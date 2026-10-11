# Cómo explorar y ejecutar los proyectos

Los notebooks, PDFs y presentaciones conservan el material académico de origen. Se han mejorado las páginas de presentación; no se han reescrito las celdas ni reentrenado los modelos.

## Lectura sin entrenamiento

Empieza por el README de cada carpeta, abre sus notebooks con las salidas guardadas y contrasta las tablas con el informe correspondiente. Los HTML y PDFs disponibles son exportaciones del material original.

## Entornos Python

Usa un entorno separado por proyecto. Los archivos `requirements.txt` identifican dependencias a partir de los imports, pero **no son un lockfile validado del entorno histórico**. Algunas APIs pueden necesitar una versión compatible con las celdas originales.

Ejemplo desde la raíz, para el proyecto de series temporales, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r 03-time-series-forecasting/requirements.txt
.\.venv\Scripts\python -m jupyterlab
```

Antes de ejecutar, ajusta las rutas que se describen en el README de cada proyecto. Los notebooks conservan rutas originales de Windows o Colab. Ejecuta las celdas en orden; algunos ficheros intermedios se generan durante el análisis.

## Recursos externos

| Proyecto | Recurso o adaptación necesaria |
|---|---|
| Ecosistema de IA | Ajustar tres rutas a los CSV incluidos |
| NLP clásico | Colab/Drive o adaptación local; [descarga y formato de GloVe](../02-hate-speech-detection/GLOVE.md), modelo portugués de spaCy y recursos NLTK |
| LLM locales | Servicio de Ollama, modelos Llama/Qwen y recursos de memoria suficientes |
| Series temporales | Ajustar dos rutas al CSV; generar particiones y resultados intermedios en orden |
| Fútbol | Ajustar ruta al dataset; compatibilidad con la API de pgmpy; Graphviz para gráficos |
| CNN de Fran | CIFAR-10 descargable; pesos e historiales recuperados en Drive privado, todavía sin descarga pública |
| Transfer learning de Minnie | STL-10 descargable; sus checkpoints finales no están disponibles |
| Autoencoders y clasificación sobre encoders | KMNIST descargable; pesos originales no localizados y sin enlace de descarga; es necesario reentrenar para generar nuevos pesos |
| YOLO de Minnie | `labels.zip` incluido; imágenes originales y pesos entrenados no disponibles en el portfolio |
| Conducción RL de Fran | Entorno externo; parche y dos checkpoints recuperados en Drive privado, todavía sin descarga pública |
| Navegación de robot de Minnie | Entorno externo; checkpoints originales no disponibles |
| Telemetría | Docker activo, variables `.env`, imágenes compatibles, importación de dashboard/consultas |

Consulta el [inventario de recursos de Deep Learning y las adaptaciones locales](../06-applied-deep-learning/RESOURCES.md) antes de ejecutar sus notebooks. Los bloques que cargan archivos no disponibles no pueden evaluarse con los modelos originales. Algunos pueden reentrenarse con datasets descargables, generando nuevos checkpoints.

No se ha reproducido íntegramente el entrenamiento ni la evaluación de los modelos. Las cifras se presentan como resultados del experimento académico publicado. La disponibilidad de los recursos externos puede cambiar.

## Créditos

Los notebooks conservan el trabajo compartido y los recursos del curso. Los repositorios de entornos de RL pertenecen a sus autores originales, identificados por los enlaces de las celdas. Consulta [procedencia](PROVENANCE.md) y el reparto de contribuciones en las páginas de proyecto.
