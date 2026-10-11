# Reinforcement Learning: conducción y navegación

**DQN · Double Dueling DQN · Estados visuales y vectoriales**

[← Deep Learning](../README.md) · [Notebook completo](Practical_Assignment_3%28Minnie_%26_Fran%29.ipynb) · [Informe](Report%20Assignment%203%28Minnie%20%26%20Fran%29.pdf) · [Vídeo de conducción](car_model_4.mp4)

## Contribuciones

- **Fran:** agente de conducción con entrada visual en `CarRacingObstacles-v3`, discretización de controles, replay buffer, entrenamiento y adaptación del entorno.
- **Minnie:** navegación de un robot en `IndoorRobot2025-v02`, con estados vectoriales y comparación de variantes DQN.
- **Entornos:** se utilizan los recursos externos identificados en las celdas originales; su autoría se conserva.

## Mi bloque: agente de conducción

El agente recibe imágenes RGB de 96×96 píxeles y utiliza un backbone convolucional. Se comparan variantes DQN y Double Dueling DQN, así como el control discreto frente a la discretización de controles continuos.

### Decisiones técnicas

- **31 acciones:** combinaciones de dirección, aceleración y freno, evitando acelerar y frenar simultáneamente.
- **Replay buffer en `uint8`:** almacenamiento de imágenes en CPU y conversión/normalización al muestrear el batch, para reducir memoria.
- **Ritmo de actualización y warm-up:** acumulación inicial de transiciones y actualización cada varios pasos del entorno.
- **Adaptación de Box2D:** conversión a `float` de coordenadas usadas por el entorno.
- **Aleatorización del entorno:** comparación del rendimiento dentro y fuera del dominio visual de entrenamiento.

## Resultados y lectura del experimento

El informe compara cinco configuraciones y documenta que entrenar sin aleatorización genera dificultades al evaluar entornos distintos. Reentrenar con aleatorización mejora ese comportamiento, aunque mantiene variabilidad entre episodios.

El archivo [car_model_4.mp4](car_model_4.mp4) ilustra una ejecución del modelo identificado por ese nombre. No representa automáticamente el modelo final aleatorizado ni sustituye su evaluación cuantitativa.

## Bloque de Minnie: navegación de robot

Comparación de agentes DQN y Double Dueling DQN con representación vectorial del estado, frente a obstáculos estáticos y dinámicos. El notebook y el informe conservan esta parte del trabajo colaborativo.

## Recursos necesarios para reproducirlo

El notebook se preparó para Colab y utiliza los entornos externos enlazados en sus celdas. Se han recuperado de Drive privado el parche `car_racing_obstacles.py`, `BestCarRacing_bestAvg20_model_4_generalizado.pth` y `BestCarRacing_best_model.pth`. **Todavía no se proporciona una descarga pública de esos archivos.** El nombre del checkpoint generalizado difiere de la ruta de evaluación del notebook y debe configurarse expresamente.

**Los checkpoints originales del robot de Minnie no están disponibles** en este portfolio. Sin los recursos correspondientes puede revisarse el código, las salidas, el vídeo y el informe, pero no evaluarse directamente los agentes originales. Para un entrenamiento nuevo hay que configurar el entorno, el parche cuando corresponda y las rutas locales. [Recursos y comprobación de compatibilidad](../RESOURCES.md) · [Guía general](../../docs/RUNNING.md).

Los dos checkpoints de conducción han superado la carga estricta con la clase `DQN` publicada y una inferencia sintética con 12 canales de entrada y 31 acciones. Hay que activar `use_dueling=True` expresamente. No se ha ejecutado el simulador ni vuelto a medir las recompensas. [Detalle de las pruebas](../RESOURCES.md#comprobación-de-compatibilidad).
