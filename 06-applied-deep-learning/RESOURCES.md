# Recursos externos y ejecución local

Estado revisado el 11 de octubre de 2026. El código y los informes permiten estudiar los tres trabajos. **El portfolio no ofrece todavía una descarga pública de los checkpoints originales ni del parche de conducción.** Los archivos recuperados del Drive privado de Fran se han descargado únicamente para su comprobación local.

## Disponibilidad por bloque

| Bloque | Recursos del experimento | Disponibilidad para un visitante |
|---|---|---|
| CNN de Fran, CIFAR-10 | Cuatro `arquitectura_base_CIFAR_10_best_state_c1…c4.pt` y cuatro `arquitectura_base_CIFAR_10_loss_history_c1…c4.pt` | Recuperados del Drive privado; pendientes de publicación como descargas |
| Transfer learning y middle fusion, Minnie | `best_resnet18_scratch.pth`, `best_resnet18_pretrained.pth`, `best_mobilenetv3s_scratch.pth`, `best_mobilenetv3s_pretrained.pth`, `best_middlefusion.pth` | No disponibles en este portfolio; Fran no dispone de estos pesos originales |
| AE, VAE y DAE, Fran | `ae.pth`, `vae.pth`, `dae.pth` | No localizados en el repositorio Deep-Learning ni en las búsquedas y carpetas académicas revisadas del Drive de Fran; sin descarga pública proporcionada |
| Clasificación sobre encoders, equipo | `ae_encoder_classifier.pth`, `vae_encoder_classifier.pth`, `dae_encoder_classifier.pth` | No localizados en esas fuentes; sin descarga pública proporcionada |
| YOLO, Minnie | Fotogramas del dataset original y `best.pt` de cada detector entrenado | No disponibles como recursos reproducibles en este portfolio. Solo se conserva `labels.zip`; el enlace histórico del notebook no está verificado como descarga pública |
| Conducción, Fran | `car_racing_obstacles.py`, `BestCarRacing_bestAvg20_model_4_generalizado.pth`, `BestCarRacing_best_model.pth` | Recuperados del Drive privado; pendientes de publicación como descargas |
| Navegación de robot, Minnie | Checkpoints `part2_dqn_qnet.pt`, `part2_double_qnet.pt`, `part2_double_dueling_qnet.pt` y recursos del experimento | No disponibles en este portfolio; Fran no dispone de los archivos originales |

Las búsquedas por nombre de autoencoders y clasificadores devolvieron referencias en documentos, pero no los archivos de pesos. Se revisaron también la carpeta de modelos entrenados, la del proyecto 2 y sus entregables finales. La ausencia en las fuentes revisadas no implica que no exista una copia en otra ubicación.

## Qué se puede ejecutar sin los archivos originales

- **CNN:** CIFAR-10 se descarga con Torchvision y es posible generar nuevos pesos mediante entrenamiento. La evaluación con los pesos históricos requiere disponer de ellos.
- **Transfer learning:** STL-10 y los pesos genéricos preentrenados de Torchvision son descargables; los modelos ajustados de Minnie no están disponibles. Un modelo genérico no sustituye su checkpoint final.
- **Autoencoders y clasificadores:** KMNIST se descarga con Torchvision. Se pueden entrenar los autoencoders y después los clasificadores para generar nuevos `.pth`; las celdas que cargan los pesos originales requieren esos archivos. Las visualizaciones de los modelos históricos no pueden repetirse directamente sin ellos.
- **YOLO:** las etiquetas por sí solas no permiten entrenar ni evaluar. Faltan las imágenes del dataset y los checkpoints de los detectores originales. Hay que proporcionar un dataset compatible o diseñar un experimento nuevo.
- **Conducción:** para ejecutar el agente recuperado se necesitan el parche, el entorno externo y un checkpoint compatible. Mientras no haya descarga pública de esos recursos, un visitante solo dispone del código, el informe y el vídeo.
- **Robot:** el código permite estudiar o preparar un nuevo entrenamiento con el entorno externo. La evaluación de los agentes originales requiere checkpoints que no se proporcionan.

Reentrenar genera un experimento nuevo: las semillas, versiones, hardware y particiones pueden afectar a los resultados. Las métricas históricas del informe no se presentan como resultados nuevamente reproducidos.

## Adaptaciones para una copia local

1. Instala las dependencias en un entorno separado y configura los entornos de RL según los repositorios enlazados en los notebooks.
2. Sustituye las rutas de `/content/drive/MyDrive/` y las operaciones de montaje de Drive por rutas locales. En los bloques YOLO, revisa también las rutas de entradas y salidas.
3. Ejecuta las definiciones de clases y la preparación de datos antes de cargar un `state_dict`. Para evaluar pesos existentes, omite las celdas de entrenamiento que podrían sobrescribirlos.
4. Usa `torch.load(ruta, map_location="cpu", weights_only=True)` para carga en CPU y `model.load_state_dict(state, strict=True)`. Activa `model.eval()` antes de inferir. [Documentación de PyTorch](https://docs.pytorch.org/docs/2.8/generated/torch.load.html).
5. En conducción conserva el orden de las acciones, los cuatro frames RGB apilados, el tamaño 96×96, la normalización y el modo Dueling del notebook. `use_dueling` no forma parte del `state_dict` y debe configurarse expresamente.
6. El checkpoint recuperado se llama `BestCarRacing_bestAvg20_model_4_generalizado.pth`. Configura `bestAvg20_path` con ese nombre cuando quieras evaluar ese archivo. No lo identifiques automáticamente con el checkpoint `…model_4.pth` del vídeo ni con otro experimento.
7. La celda de hiperparámetros de conducción contiene una línea aislada con `;`: elimínala en tu copia de trabajo antes de ejecutar esa celda en Python.

## Comprobación de compatibilidad

**Resultado del 11 de octubre de 2026:** los seis checkpoints de modelos son compatibles estructuralmente con las clases publicadas; los cuatro historiales se cargan correctamente. [Informe completo en JSON](checkpoint-compatibility.json).

| Recurso comprobado | Resultado |
|---|---|
| CNN `c1`, `c2`, `c3`, `c4` | Carga estricta sin claves faltantes, inesperadas ni dimensiones distintas; entrada `[2, 3, 32, 32]`, salida `[2, 10]`, pesos y salidas finitos |
| Cuatro historiales de CNN | `train_losses` y `val_losses` válidos, con 15 épocas cada uno |
| Dos checkpoints de conducción | Carga estricta sin incompatibilidades; entrada `[2, 12, 96, 96]`, salida `[2, 31]`, pesos y salidas finitos con Dueling activado |

La prueba se ejecutó con Python 3.12.3 y PyTorch 2.8.0 para CPU. Estos son los componentes utilizados para la comprobación, no un entorno completo validado para entrenar todos los proyectos. Los checksums del informe permiten identificar exactamente los archivos comprobados.

El script [check_checkpoints.py](tools/check_checkpoints.py) extrae exclusivamente las clases `SimpleCifarCNN` y `DQN` de los notebooks publicados. No ejecuta sus celdas de montaje, entrenamiento ni descarga.

Con los diez archivos recuperados en una misma carpeta, desde la raíz del portfolio:

```powershell
python 06-applied-deep-learning/tools/check_checkpoints.py --resources checkpoints --report checkpoint-check.json
```

Comprueba nombres y dimensiones de los parámetros, carga estricta, valores finitos e inferencia con entradas sintéticas; también comprueba las series de pérdidas. Necesita PyTorch. Una comprobación favorable confirma compatibilidad estructural, pero no valida accuracy, rewards ni la configuración histórica de entrenamiento. No ejecuta CIFAR-10 ni episodios del simulador.
