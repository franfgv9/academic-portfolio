# Descarga y uso de GloVe

El notebook de ML clásico utiliza embeddings en portugués de 100 dimensiones. El recurso es externo y pertenece a sus autores; no se incluye un modelo de embeddings dentro del historial Git del portfolio.

## Distribución pública actual de NILC

[Modelo GloVe 100d de NILC](https://huggingface.co/nilc-nlp/glove-100d) · [Archivos para descargar](https://huggingface.co/nilc-nlp/glove-100d/tree/4b9adabf3fec33a74ab40d9841a52993f0bea62d)

La distribución actual contiene `embeddings.safetensors` y `vocab.txt`. **No es un archivo `glove_s100.txt` y no puede cargarse directamente con `load_word2vec_format`.** Su ficha indica licencia CC BY 4.0 y atribuye el recurso a NILC y a Hartmann et al. (2017), *Portuguese Word Embeddings: Evaluating on Word Analogies and Natural Language Tasks*. [Trabajo y recursos de los autores](https://github.com/nathanshartmann/portuguese_word_embeddings).

Para utilizar esta distribución, instala las dependencias adicionales en el entorno del proyecto:

```powershell
python -m pip install huggingface_hub safetensors
```

En una copia de trabajo del notebook, sustituye únicamente la celda que carga `glove_path` y `w2v_model` por:

```python
from huggingface_hub import hf_hub_download
from safetensors.numpy import load_file
from gensim.models import KeyedVectors

repo_id = "nilc-nlp/glove-100d"
revision = "4b9adabf3fec33a74ab40d9841a52993f0bea62d"
matrix_path = hf_hub_download(repo_id, "embeddings.safetensors", revision=revision)
vocab_path = hf_hub_download(repo_id, "vocab.txt", revision=revision)

vectors = load_file(matrix_path)["embeddings"]
with open(vocab_path, encoding="utf-8") as file:
    vocabulary = [line.strip() for line in file]

if vectors.shape != (len(vocabulary), 100):
    raise ValueError("El vocabulario y la matriz de embeddings no son compatibles")

w2v_model = KeyedVectors(vector_size=100)
w2v_model.add_vectors(vocabulary, vectors)
```

Este código adapta el formato a la interfaz de Gensim usada por las celdas posteriores. La revisión está fijada para que la descarga no cambie al actualizarse el modelo remoto. Se necesita memoria para cargar tanto la matriz como la copia de Gensim.

**No se ha comprobado que esta distribución sea numéricamente idéntica al fichero histórico del experimento ni se ha repetido su evaluación.** Al emplearla, registra el recurso y la revisión utilizados, y calcula de nuevo las métricas.

## Fichero histórico del experimento

El archivo conservado por Fran es `glove_s100.txt`, recibido durante la asignatura de PLN de Coimbra. El material de la práctica identifica el modelo como GloVe de NILC, distribuido entonces mediante UCStudent.

| Propiedad comprobada | Valor |
|---|---|
| Cabecera | `934963 100` |
| Tamaño del TXT | 896.435.591 bytes |
| Tamaño del ZIP adjuntado | 350.667.337 bytes |
| SHA-256 del TXT | `baf73822e7082b9dcf1bdd2585cdaa4e01d8b5463b7e504c9740141527a6a907` |
| SHA-256 del ZIP | `a37648d1f5d1850bf29036bb22740f3b715b0eb74b0125e1b0da1338a28d2bad` |

No se ha verificado una descarga pública del fichero histórico exacto. El enlace anterior corresponde a la distribución pública actual de NILC.

Si ya dispones del TXT original, sitúalo en `02-hate-speech-detection/data/glove_s100.txt` y, al abrir el notebook desde `code/`, configura:

```python
glove_path = "../data/glove_s100.txt"
w2v_model = KeyedVectors.load_word2vec_format(glove_path)
```

Si recibes el ZIP original, extrae solo `glove_s100.txt`; la carpeta `__MACOSX` no es necesaria. Puedes comprobar la integridad en PowerShell:

```powershell
Get-FileHash -LiteralPath "02-hate-speech-detection/data/glove_s100.txt" -Algorithm SHA256
```
