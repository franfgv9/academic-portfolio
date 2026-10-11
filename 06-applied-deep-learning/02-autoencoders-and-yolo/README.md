# Representaciones latentes y detección de objetos

**Autoencoders · VAE · DAE · t-SNE · YOLO**

[← Deep Learning](../README.md) · [Notebook completo](code/Practical_Assignment_2%28minnie_%26_fran%29.ipynb) · [Informe](Report-Assignment2.pdf) · [Presentación](Report-Assignment2.pptx)

## Contribuciones

- **Fran:** implementación y entrenamiento de AE, VAE y DAE sobre Kuzushiji-MNIST; reconstrucción, denoising y análisis del espacio latente.
- **Minnie:** dataset y anotación de personas, pipeline de detección y comparación de YOLOv8/9/10.
- **Evaluación complementaria de los encoders:** trabajo compartido, con la incorporación del clasificador sobre encoders congelados por Minnie.

## Mi bloque: AE, VAE y DAE

Los modelos comparten un backbone convolucional y un espacio latente de 32 dimensiones, permitiendo comparar el efecto de la reconstrucción, la regularización variacional y el entrenamiento con ruido. Se incluyen visualizaciones t-SNE y ejemplos de reconstrucción/denoising.

La tabla de evaluación del informe registra aproximadamente 89,13% de accuracy para el clasificador sobre el encoder AE, 87,89% para VAE y 87,26% para DAE. Son resultados del protocolo académico compartido. El rendimiento del clasificador y la calidad generativa o de denoising miden propiedades distintas.

## Bloque de Minnie: detección de personas

Anotación asistida con Roboflow y comparación de modelos YOLO entrenados desde cero o con pesos preentrenados. El informe registra mAP50-95 de 0,4206 y unas 0,17 horas de entrenamiento para YOLOv8s en la configuración documentada. Estas cifras corresponden al bloque de Minnie y dependen del dataset y el hardware del experimento.

## Cómo explorar y ejecutar

El notebook usa Colab/Drive. **Los pesos originales de AE, VAE, DAE y los clasificadores sobre encoders no están disponibles y no tienen un enlace de descarga.** Para ejecutar las celdas de evaluación hay que generar nuevos pesos mediante entrenamiento con KMNIST o disponer de esos archivos por otra vía.

**El dataset de imágenes y los checkpoints YOLO de Minnie tampoco están disponibles en este portfolio.** Se conserva [labels.zip](labels.zip), pero las etiquetas solas no permiten entrenar ni evaluar. El notebook contiene un enlace histórico externo al dataset; no está verificado como descarga pública utilizable.

Configura las rutas y ejecuta cada parte en orden. Las dependencias de Python se describen en [requirements.txt](../requirements.txt). [Inventario de recursos y ejecución local](../RESOURCES.md) · [Guía general](../../docs/RUNNING.md).
