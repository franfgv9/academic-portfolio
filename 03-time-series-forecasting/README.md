# Forecasting del IPC de Chile

**Series temporales · SARIMA · Suavizado exponencial · Evaluación temporal**

[← Portfolio](../README.md) · [Notebook](code/FRANCISCO_GIL.ipynb) · [Informe IEEE](IEEE_report_forecasting.pdf) · [Notebook en PDF](code/FRANCISCO_GIL.pdf)

## Qué problema aborda

Analizar y predecir el IPC mensual de Chile, comparando enfoques sencillos y modelos temporales. El informe estudia **392 observaciones de enero de 1990 a agosto de 2022**, además de una comparación multivariante con México, Colombia y Brasil.

## Mi contribución

Proyecto individual de **Francisco Gil Valverde**: preparación de la serie, análisis descriptivo y estacionariedad, modelado, comparación de previsiones, exploración multivariante e informe.

## Metodología

1. Selección y preparación de la serie mensual del IPC.
2. Descomposición, estacionalidad y pruebas de estacionariedad.
3. Baseline por extrapolación, SARIMA y triple suavizado exponencial multiplicativo.
4. Comparación de forecast directo a 24 meses y evaluación rolling one-step-ahead.
5. Análisis de inflación mensual y relaciones temporales entre países.

## Resultados

| Evaluación rolling sobre test | RMSE | MAPE |
|---|---:|---:|
| SARIMA | **0,537** | **0,366%** |
| Triple suavizado exponencial | 1,477 | 1,019% |

En el forecast directo a **24 meses**, el suavizado multiplicativo obtuvo menor error. En la evaluación rolling, SARIMA rindió mejor. Son problemas de predicción distintos: en rolling se incorpora información observada antes de cada nueva predicción.

Los modelos infraestimaron parte de la aceleración final del IPC. El informe también muestra que los intervalos no alcanzaron la cobertura nominal del 95%. Estas limitaciones ayudan a interpretar el rendimiento frente a cambios de dinámica.

## Archivos y ejecución

El notebook conserva los gráficos y resultados del experimento. La entrada principal está en `data/CPITimeSeries.csv`; las particiones y tablas intermedias se generan al ejecutar las celdas anteriores.

Para volver a ejecutarlo desde `code/`, instala `requirements.txt` y ajusta las **dos** lecturas de `CPITimeSeries.csv` a `../data/CPITimeSeries.csv`. Mantén el orden de las celdas para generar los CSV intermedios antes de leerlos. [Guía general](../docs/RUNNING.md).

**Stack:** Python, Pandas, NumPy, statsmodels, SciPy, scikit-learn y Matplotlib.
