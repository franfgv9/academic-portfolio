"""Check recovered CNN/CarRacing weights against the published notebook classes.

Loads state dictionaries on CPU with weights_only=True. Does not train models,
download datasets, execute notebook setup cells, or run Gym environments.
"""
import argparse
import ast
import hashlib
import json
import math
import platform
import re
from pathlib import Path

import torch
from torch import nn
from torch.nn import functional as F

PROJECT = Path(__file__).resolve().parents[1]
CNN = PROJECT / "01-cnn-and-transfer-learning/code/Practical_Assignment_1(Minnie&Fran).ipynb"
RL = PROJECT / "03-reinforcement-learning/Practical_Assignment_3(Minnie_&_Fran).ipynb"


def notebook_class(path, name):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        if not re.search(r"^class " + re.escape(name) + r"\(", source, re.M):
            continue
        tree = ast.parse(source)
        node = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name)
        module = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
        namespace = {"torch": torch, "nn": nn, "F": F}
        exec(compile(module, str(path), "exec"), namespace)
        return namespace[name]
    raise ValueError(f"Class {name} not found in {path.name}")


def literal_config(path, key):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    values = []
    for cell in notebook["cells"]:
        source = "".join(cell.get("source", []))
        for match in re.finditer(r"^" + re.escape(key) + r"\s*=\s*([^;#\n]+)", source, re.M):
            values.append(ast.literal_eval(match.group(1).strip()))
    if not values or len(set(values)) != 1:
        raise ValueError(f"Ambiguous notebook configuration: {key}")
    return values[0]


def file_properties(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": digest.hexdigest()}


def check_weights(path, model, sample, expected_output):
    result = file_properties(path)
    state = torch.load(path, map_location="cpu", weights_only=True)
    expected = model.state_dict()
    missing = sorted(set(expected) - set(state))
    unexpected = sorted(set(state) - set(expected))
    mismatches = {
        key: {"expected": list(expected[key].shape), "actual": list(state[key].shape)}
        for key in set(expected) & set(state)
        if expected[key].shape != state[key].shape
    }
    result.update(missing_keys=missing, unexpected_keys=unexpected, shape_mismatches=mismatches)
    if missing or unexpected or mismatches:
        result["compatible"] = False
        return result
    finite = all(not t.is_floating_point() or bool(torch.isfinite(t).all()) for t in state.values())
    model.load_state_dict(state, strict=True)
    model.eval()
    with torch.inference_mode():
        output = model(sample)
    result.update(
        state_entries=len(state), input_shape=list(sample.shape), output_shape=list(output.shape),
        finite_weights=finite, finite_output=bool(torch.isfinite(output).all()),
        compatible=finite and tuple(output.shape) == expected_output and bool(torch.isfinite(output).all()),
    )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resources", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    torch.set_num_threads(2)
    torch.manual_seed(79)
    cnn_class = notebook_class(CNN, "SimpleCifarCNN")
    dqn_class = notebook_class(RL, "DQN")
    channels = literal_config(RL, "FrameSize") * literal_config(RL, "FrameStack")
    continuous = literal_config(RL, "UseContinuousControl")
    dueling = literal_config(RL, "useDueling")
    # Notebook action table: 5 steering values x (4 gas + 2 brake) + 1 recovery.
    n_actions = 5 * (4 + 2) + 1 if continuous else 5
    cnn_sample = torch.randn(2, 3, 32, 32)
    rl_sample = torch.randint(0, 256, (2, channels, 96, 96), dtype=torch.uint8)
    report = {
        "python": platform.python_version(), "torch": torch.__version__, "device": "cpu",
        "notebooks": [file_properties(CNN), file_properties(RL)],
        "rl_configuration": {"input_channels": channels, "actions": n_actions, "use_dueling": dueling},
        "checks": [],
        "scope": "Strict state_dict load, finite tensors and synthetic inference; no dataset evaluation or environment rollout.",
    }
    for config in range(1, 5):
        name = f"arquitectura_base_CIFAR_10_best_state_c{config}.pt"
        report["checks"].append(check_weights(args.resources / name, cnn_class(), cnn_sample, (2, 10)))
        history = args.resources / f"arquitectura_base_CIFAR_10_loss_history_c{config}.pt"
        data = torch.load(history, map_location="cpu", weights_only=True)
        train = data["train_losses"]
        validation = data["val_losses"]
        valid = len(train) > 0 and len(train) == len(validation) and all(math.isfinite(float(v)) for v in [*train, *validation])
        report["checks"].append({**file_properties(history), "history_keys": sorted(data), "epochs": len(train), "compatible": valid})
    for name in ["BestCarRacing_bestAvg20_model_4_generalizado.pth", "BestCarRacing_best_model.pth"]:
        model = dqn_class(channels, n_actions)
        model.use_dueling = dueling
        report["checks"].append(check_weights(args.resources / name, model, rl_sample, (2, n_actions)))
    report["all_compatible"] = all(c["compatible"] for c in report["checks"])
    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.report:
        args.report.write_text(text + "\n", encoding="utf-8")
    print(text)
    raise SystemExit(0 if report["all_compatible"] else 1)


if __name__ == "__main__":
    main()
