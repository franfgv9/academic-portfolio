# Parche del entorno de conducción

[car_racing_obstacles.py](car_racing_obstacles.py) es el archivo modificado utilizado por Fran en su proyecto académico. Se conserva byte a byte desde la copia recuperada de su Drive.

## Procedencia y atribución

El entorno de base procede de [luisgarrote/CarRacingWObstacles](https://github.com/luisgarrote/CarRacingWObstacles) y utiliza los componentes de CarRacing, Gymnasium y Box2D. La autoría del entorno corresponde a sus autores originales. La adaptación académica de Fran incluye conversiones a `float` de coordenadas para Box2D; no se presenta el entorno completo como una creación propia.

SHA-256 del archivo conservado:

```text
038853aa4340f81721b0424d723cbc6e95c327e7acbf924f42ab8e09943d9af4
```

## Instalación local

Este archivo depende de `car_racing.py` y `car_dynamics.py` del entorno externo; no es un módulo autónomo. Instala las dependencias indicadas por ese entorno. Desde la raíz del portfolio, puedes colocar la copia externa y aplicar el parche así:

```powershell
New-Item -ItemType Directory -Force -Path external | Out-Null
git clone https://github.com/luisgarrote/CarRacingWObstacles.git external/CarRacingWObstacles
Copy-Item -LiteralPath "06-applied-deep-learning/03-reinforcement-learning/patches/car_racing_obstacles.py" -Destination "external/CarRacingWObstacles/car_racing_obstacles.py"
python -m pip install -e ./external/CarRacingWObstacles
```

Si ya tienes una copia de ese entorno, aplica el parche sobre ella sin repetir el clon. En una copia local del notebook, sustituye la ruta de `PATCH_FILE` por la ruta absoluta a este archivo y omite el montaje de Drive y la instalación de Colab que hayas realizado localmente. Conserva el registro del entorno que aparece en sus celdas.

La copia del parche se ha comprobado por SHA-256 y su sintaxis Python es válida. Las pruebas de checkpoints verificaron las redes, sin ejecutar episodios de este entorno. Consulta [recursos y ejecución local](../../RESOURCES.md) para descargar pesos y configurar la inferencia.
