# Autoría, fuentes y alcance

Este portfolio reúne seis proyectos académicos de ciencia de datos e inteligencia artificial. Cada página de proyecto enlaza su código, informes y resultados, e identifica las contribuciones individuales y compartidas.

## Autoría de los proyectos

| Proyecto | Autoría |
|---|---|
| [Ecosistema de IA](../01-ai-ecosystem-spain/) | Francisco Gil Valverde y Gastón Fernández Rodríguez |
| [Detección de lenguaje ofensivo](../02-hate-speech-detection/) | Francisco Gil Valverde y Gastón Fernández Rodríguez |
| [Forecasting del IPC de Chile](../03-time-series-forecasting/) | Francisco Gil Valverde |
| [Forecasting probabilístico de fútbol](../04-probabilistic-ai-forecasting/) | Francisco Gil Valverde; los scripts auxiliares mantienen su procedencia |
| [Telemetría lunar](../05-lunar-telemetry-pipeline/) | Proyecto académico presentado por Francisco Gil Valverde |
| [Deep Learning y Reinforcement Learning](../06-applied-deep-learning/) | Francisco Gil Valverde y Minnie; contribuciones detalladas por bloque |

En Deep Learning, mi contribución comprende la CNN sobre CIFAR-10, los autoencoders AE/VAE/DAE y el agente visual de conducción. Minnie desarrolló transfer learning y middle fusion, detección con YOLO y navegación del robot. La clasificación sobre encoders forma parte de la evaluación compartida, con la contribución de Minnie identificada en su proyecto.

En los trabajos de equipo, las métricas corresponden al experimento conjunto. Cuando los informes no detallan el reparto individual, no se atribuyen componentes concretos en exclusiva.

## Recursos externos

Los datasets, modelos preentrenados y recursos del curso conservan la autoría y las condiciones de sus fuentes. Los notebooks e informes incluyen los enlaces utilizados en cada experimento.

- Los embeddings en portugués proceden de NILC. La [guía de GloVe](../02-hate-speech-detection/GLOVE.md) incluye la distribución pública actual y la referencia de Hartmann et al. (2017).
- El entorno de conducción procede de [luisgarrote/CarRacingWObstacles](https://github.com/luisgarrote/CarRacingWObstacles), sobre componentes de CarRacing, Gymnasium y Box2D. El [parche académico](../06-applied-deep-learning/03-reinforcement-learning/patches/) documenta sus adaptaciones y procedencia.
- Los entornos y recursos de navegación del robot se identifican en las celdas del notebook de Reinforcement Learning.

## Interpretación de los resultados

Las métricas de los README corresponden a los experimentos documentados en sus informes. Cada proyecto describe el conjunto evaluado y sus limitaciones; las cifras de distintos datasets o protocolos no son directamente comparables.

Los checkpoints publicados de CNN y conducción han superado carga estricta e inferencia sintética. Estas pruebas confirman compatibilidad estructural y no sustituyen una evaluación sobre datos o episodios del simulador. Consulta [recursos y comprobaciones](../06-applied-deep-learning/RESOURCES.md) y la [guía de ejecución](RUNNING.md).
