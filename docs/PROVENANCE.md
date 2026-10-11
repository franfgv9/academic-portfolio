# Créditos y procedencia

## Copia de origen

- Repositorio: https://github.com/franfgv9/data-science-portfolio
- Commit de origen: `e9d1b729b9376600072a525f146d254621f06c25`.
- Fecha de preparación: 11 de octubre de 2026.
- Destino propuesto: `franfgv9/academic-portfolio`, independiente del perfil y del repositorio de origen.

Se conservan los seis directorios académicos, sus notebooks, scripts, datasets, PDFs, presentaciones y vídeo. Los README principales y los tres de Deep Learning se han redactado de nuevo. Se añaden navegación, portadas, dependencias documentales y textos para LinkedIn.

El origen se utilizó en modo lectura y permanece intacto. Esta copia no comparte historial de trabajo ni sincroniza cambios con el repositorio original.

## Autoría

| Proyecto | Evidencia de autoría |
|---|---|
| Ecosistema de IA | Informe: Francisco Gil Valverde y Gastón Fernández Rodríguez; reparto por tareas no documentado |
| NLP | Informe de ML: Francisco Gil Valverde y Gastón Fernández Rodríguez; reparto por tareas no documentado |
| Series temporales | Informe individual de Francisco Gil Valverde |
| Fútbol | Informe individual de Francisco Gil; los scripts auxiliares mantienen su procedencia original |
| Telemetría | Publicación de Fran; el informe no identifica el reparto de tareas |
| Deep Learning | Minnie y Fran; reparto explicado y confirmado por Fran durante la preparación |

Se conserva la atribución a Minnie de transfer learning/middle fusion, YOLO y navegación de robot. La evaluación de clasificación sobre los encoders se mantiene como trabajo compartido y atribuido a Minnie en el README de origen. Las métricas del equipo no implican autoría individual de cada componente.

## Precisiones respecto a la presentación anterior

- Qwen: F1 macro ≈ 0,880 sobre 75 ejemplos; ML clásico sobre el test completo.
- Fútbol: el 68,24% corresponde a abstención por confianza y al 50,45% de decisiones aceptadas; la estrategia híbrida tiene cifras distintas.
- Autoencoders: se prioriza la tabla del informe (AE ≈ 0,8913) frente al redondeo anterior (~0,889).
- Telemetría: redes lógicas de Docker con Telegraf como puente; se evita describirlo como air gap físico.
- Los nombres y rutas enlazados corresponden a archivos existentes; se sustituyen los árboles ficticios del README anterior.
- La cifra 692,14 aparece en el README anterior de RL. No se usa como cifra principal del nuevo portfolio al no haberse vinculado aquí a una tabla exacta de evaluación; se conserva el informe para revisión.
- El vídeo de RL es `car_model_4.mp4`; no se identifica como vídeo del modelo 5.

## Datos y licencias

El repositorio original no contiene una licencia general. Esta copia no añade una licencia que conceda derechos sobre datasets, material del curso o aportaciones de terceros. Se conservan los créditos y deben respetarse las condiciones de las fuentes originales.

## Verificación

`source-manifest.json` registra los hashes de los archivos del origen. Las comprobaciones locales se guardan en `REVIEW.md`. El hecho de conservar salidas o informes no equivale a haber repetido los experimentos.

## Recursos de Deep Learning recuperados

El 11 de octubre de 2026 se recuperaron del Drive académico de Fran cuatro checkpoints de CNN, cuatro historiales y dos checkpoints de conducción. Se publican como descargas en la [Release de recursos](https://github.com/franfgv9/academic-portfolio/releases/tag/dl-resources-v1), con manifiestos SHA-256 e informe de compatibilidad estructural. Los notebooks del origen se conservan sin modificaciones.

Se añade el archivo modificado [car_racing_obstacles.py](../06-applied-deep-learning/03-reinforcement-learning/patches/car_racing_obstacles.py), byte a byte desde la copia de Fran, con atribución al entorno externo `luisgarrote/CarRacingWObstacles` y sus componentes de base. Las adaptaciones académicas no implican autoría del entorno completo. Consulta los [créditos e instrucciones del parche](../06-applied-deep-learning/03-reinforcement-learning/patches/).

Las descargas no incluyen los pesos originales que no se han localizado ni los archivos de Minnie que Fran no conserva. Su ausencia se documenta en [RESOURCES.md](../06-applied-deep-learning/RESOURCES.md).
