# Clasificación de imágenes: CNN y transfer learning

**CIFAR-10 · STL-10 · PyTorch · Middle fusion**

[← Deep Learning](../README.md) · [Notebook completo](code/Practical_Assignment_1%28Minnie%26Fran%29.ipynb) · [Exportación HTML](code/Practical_Assignment_1%28Minnie%26Fran%29.html) · [Informe](Report-Practical%20Assignment%201%28Minnie%20%26%20Fran%29.pdf)

## Contribuciones

- **Fran:** diseño, entrenamiento y evaluación de la CNN sobre CIFAR-10; experimentos con hiperparámetros y data augmentation.
- **Minnie:** comparación de transfer learning y arquitectura de middle fusion con ResNet18 y MobileNetV3-Small sobre STL-10.

El notebook contiene ambas partes del trabajo, con sus salidas guardadas.

## Mi bloque: CNN sobre CIFAR-10

Se diseñó una red con tres bloques convolucionales de filtros crecientes, Batch Normalization, ReLU y Max Pooling, seguida de capas fully connected y Dropout. Se compararon cuatro configuraciones de entrenamiento y se aplicaron Random Crop, Horizontal Flip y Color Jitter.

| Métrica de la CNN de Fran | Valor del informe |
|---|---:|
| Accuracy | 89,35% |
| Mean Class Accuracy | 86,18% |
| F1 | 86,16% |

El informe documenta una partición de 40.000 imágenes de entrenamiento, 10.000 de validación y 10.000 de test. Las cifras corresponden a la evaluación registrada del experimento; no se han vuelto a calcular durante esta preparación.

## Bloque de Minnie: transfer learning y middle fusion

Comparación de modelos desde cero y con pesos preentrenados, seguida de fusión de representaciones de ResNet18 y MobileNetV3-Small. El informe registra 96,1% de accuracy para middle fusion sobre STL-10. Es un resultado del bloque de Minnie y de un dataset distinto al de la CNN.

## Cómo explorar y ejecutar

El notebook original usa Colab y guarda/carga checkpoints en Drive. **[Descarga los cuatro checkpoints de CNN de Fran y sus historiales](https://github.com/franfgv9/academic-portfolio/releases/download/dl-resources-v1/cnn-checkpoints.zip)** y configura `save_dir` con la ruta absoluta a la carpeta local donde los extraigas. Para evaluarlos, ejecuta la definición de la red y la preparación de datos y omite el entrenamiento que sobrescribe los archivos. Los checkpoints de transfer learning y middle fusion de Minnie **no están disponibles** en este portfolio.

Para generar nuevos pesos, instala las dependencias del [directorio de Deep Learning](../requirements.txt), configura las rutas locales y ejecuta el entrenamiento. CIFAR-10 y STL-10 se descargan mediante Torchvision. Los pesos genéricos preentrenados de Torchvision no sustituyen los modelos finales ajustados de Minnie. [Recursos y ejecución local](../RESOURCES.md) · [Guía general](../../docs/RUNNING.md).

La exportación HTML y el informe permiten consultar resultados sin disponer de los checkpoints.

Los cuatro checkpoints de Fran han superado la carga estricta y una inferencia con entradas sintéticas; los cuatro historiales son válidos. Esta comprobación confirma compatibilidad estructural, sin volver a medir accuracy. [Detalle de las pruebas](../RESOURCES.md#comprobación-de-compatibilidad).
