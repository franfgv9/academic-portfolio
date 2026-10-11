# Forecasting probabilístico de fútbol

**Redes bayesianas · Calibración · Conformal Prediction · Abstención**

[← Portfolio](../README.md) · [Notebook](code/probabilistic_forecasting.ipynb) · [Informe](Final_Report_Francisco_Gil.pdf) · [Notebook en PDF](code/probabilistic_forecasting.pdf)

## Qué problema aborda

Estimar las probabilidades de victoria local, empate y victoria visitante en partidos de la liga portuguesa. El proyecto estudia la incertidumbre, la calidad de las probabilidades y cuándo conviene abstenerse de emitir una predicción.

## Mi contribución

Proyecto individual: exploración de datos, redes bayesianas manuales y aprendidas, inferencia, clasificación probabilística, calibración, optimización y evaluación de estrategias de decisión. Incluye el notebook, el informe y los scripts auxiliares de preparación de datos.

## Metodología

```mermaid
flowchart LR
    A[Datos y variables] --> B[Redes bayesianas y Naive Bayes]
    B --> C[Calibración e incertidumbre]
    C --> D[Evaluación y abstención]
```

- Comparación de conocimiento de dominio y aprendizaje de estructura con Hill Climbing.
- Estimación de parámetros e inferencia en redes bayesianas.
- Naive Bayes, Split Conformal Prediction y Platt Scaling.
- Optimización bayesiana y análisis exploratorio de utilidad con cuotas.

## Resultados y límites

| Experimento | Resultado registrado |
|---|---|
| Platt Scaling | Log Loss: **1,1452 → 0,9556**; ECE: **0,1241 → 0,0340** |
| Split Conformal Prediction | Cobertura empírica **90,25%**; tamaño medio del conjunto **2,2637** entre tres clases |
| Predecir todos los partidos | Accuracy **55,02%**, cobertura de decisión **100%** |
| Abstención por confianza | Accuracy **68,24%** en el **50,45%** de partidos aceptados |
| Estrategia híbrida con cuotas | Accuracy **55,56%** en el **73,43%** de partidos aceptados |

El 68,24% pertenece a la **abstención por confianza**, no a la estrategia híbrida. Mejorar la precisión implica reducir la cobertura de decisión. Los conjuntos conformales suelen ser amplios y los empates siguen siendo difíciles de predecir.

La cobertura conformal y la cobertura de decisión describen cosas diferentes: la primera mide si la clase real está dentro del conjunto; la segunda, cuántos partidos reciben una decisión. El análisis de cuotas es académico y exploratorio; no demuestra rentabilidad futura.

## Archivos y ejecución

`data/dataset.csv` contiene la entrada del notebook. Instala `requirements.txt` y ejecuta desde `code/`, cambiando la lectura de `dataset.csv` a `../data/dataset.csv`. La visualización con Graphviz puede requerir además su ejecutable en el sistema.

Los scripts de `code/data_preparation/` conservan rutas de la preparación original: requieren adaptarlas y disponer de los CSV de partidos antes de reconstruir los datos. El notebook puede explorarse directamente con el dataset incluido. [Guía general](../docs/RUNNING.md).

**Stack:** Python, pgmpy, scikit-learn, scikit-optimize, Pandas, NumPy, Matplotlib y Graphviz.
