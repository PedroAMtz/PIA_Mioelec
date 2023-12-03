# PIA Mioelectricidad :zap:
---

### Set-up de entorno virtual :wrench:
#### Configuración del entorno de desarrollo

1. **Instalar Pipenv**: Si no lo tienes instalado, instala Pipenv usando pip, el administrador de paquetes de Python. Abre la línea de comandos y ejecuta:

    ```sh
    pip install pipenv
    ```

2. **Clonar el repositorio**: Clona el repositorio en tu máquina local. Abre la línea de comandos, navega al directorio donde quieres clonar el repositorio y ejecuta:

    ```sh
    git clone <url-del-repositorio>
    cd <nombre-del-repositorio>
    ```

3. **Instalar dependencias**: Instala todas las dependencias del proyecto usando el comando `pipenv install`. Este comando creará un entorno virtual si no existe uno y luego instalará todas las dependencias listadas en el `Pipfile.lock`. Abre la línea de comandos y ejecuta:

    ```sh
    pipenv install
    ```

4. **Activar el entorno virtual**: Para activar el entorno virtual creado por Pipenv, ejecuta el siguiente comando en la línea de comandos:

    ```sh
    pipenv shell
    ```

    Ahora estarás en el entorno virtual y podrás ejecutar el código del proyecto.

5. **Instalar dependencias con requirements.txt (alternativa)**: Si prefieres usar `requirements.txt`, puedes instalar todas las dependencias listadas en este archivo usando pip. Primero, crea un entorno virtual usando el comando `python -m venv` y luego actívalo. Después de eso, instala las dependencias usando pip. Abre la línea de comandos y ejecuta:

    ```sh
    pip install -r requirements.txt
    ```

Ahora estarás en el entorno virtual y podrás ejecutar el código del proyecto.


### Resultados modelos de clasificación :bar_chart:

---

#### Modelo SVM 

![curvas aprendizaje svm](learning_curves_svm.png)

![svm confusion matrix](svm_cm.png)

**Reporte de Clasificación:**

|           | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| A         | 0.82      | 0.82   | 0.82     | 11      |
| B         | 0.80      | 0.67   | 0.73     | 6       |
| C         | 0.75      | 0.90   | 0.82     | 10      |
| D         | 0.86      | 0.67   | 0.75     | 9       |
| E         | 0.50      | 0.75   | 0.60     | 4       |
| F         | 0.83      | 0.67   | 0.74     | 15      |
| G         | 0.86      | 0.67   | 0.75     | 9       |
| H         | 0.86      | 0.67   | 0.75     | 9       |
| I         | 1.00      | 0.83   | 0.91     | 12      |
| J         | 1.00      | 1.00   | 1.00     | 8       |
| K         | 1.00      | 0.60   | 0.75     | 10      |
| L         | 0.67      | 0.80   | 0.73     | 5       |
| M         | 0.80      | 1.00   | 0.89     | 4       |
| N         | 0.44      | 0.80   | 0.57     | 5       |
| O         | 0.57      | 0.80   | 0.67     | 5       |
| P         | 0.70      | 0.88   | 0.78     | 8       |
| Q         | 0.57      | 0.67   | 0.62     | 6       |
| R         | 0.67      | 1.00   | 0.80     | 6       |
| S         | 1.00      | 0.70   | 0.82     | 10      |
| T         | 0.67      | 0.75   | 0.71     | 8       |
| U         | 1.00      | 0.70   | 0.82     | 10      |
| V         | 0.83      | 1.00   | 0.91     | 5       |
| W         | 1.00      | 0.80   | 0.89     | 5       |
| X         | 0.88      | 0.78   | 0.82     | 9       |
| Y         | 0.92      | 0.92   | 0.92     | 12      |
| Z         | 0.70      | 1.00   | 0.82     | 7       |
| Ñ         | 0.78      | 0.88   | 0.82     | 8       |
| Accuracy  |           |        | 0.79     | 216     |
| Macro Avg | 0.79      | 0.80   | 0.79     | 216     |
| Weighted Avg | 0.82   | 0.79   | 0.79     | 216     |

#### Modelo GBM 

![gbm confusion matrix](gbm_cm.png)

**Reporte de Clasificación:**

|           | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| 0         | 0.82      | 0.82   | 0.82     | 11      |
| 1         | 0.80      | 0.67   | 0.73     | 6       |
| 2         | 0.64      | 0.90   | 0.75     | 10      |
| 3         | 0.86      | 0.67   | 0.75     | 9       |
| 4         | 1.00      | 0.75   | 0.86     | 4       |
| 5         | 1.00      | 0.67   | 0.80     | 15      |
| 6         | 0.78      | 0.78   | 0.78     | 9       |
| 7         | 0.86      | 0.67   | 0.75     | 9       |
| 8         | 0.83      | 0.83   | 0.83     | 12      |
| 9         | 0.78      | 0.88   | 0.82     | 8       |
| 10        | 0.86      | 0.60   | 0.71     | 10      |
| 11        | 0.67      | 0.80   | 0.73     | 5       |
| 12        | 0.80      | 1.00   | 0.89     | 4       |
| 13        | 0.43      | 0.60   | 0.50     | 5       |
| 14        | 0.57      | 0.80   | 0.67     | 5       |
| 15        | 0.78      | 0.88   | 0.82     | 8       |
| 16        | 0.80      | 0.67   | 0.73     | 6       |
| 17        | 0.71      | 0.83   | 0.77     | 6       |
| 18        | 0.78      | 0.70   | 0.74     | 10      |
| 19        | 0.67      | 0.75   | 0.71     | 8       |
| 20        | 0.88      | 0.70   | 0.78     | 10      |
| 21        | 0.62      | 1.00   | 0.77     | 5       |
| 22        | 1.00      | 0.80   | 0.89     | 5       |
| 23        | 0.67      | 0.67   | 0.67     | 9       |
| 24        | 0.92      | 0.92   | 0.92     | 12      |
| 25        | 1.00      | 1.00   | 1.00     | 7       |
| 26        | 0.70      | 0.88   | 0.78     | 8       |
| Accuracy  |           |        | 0.78     | 216     |
| Macro Avg | 0.79      | 0.79   | 0.78     | 216     |
| Weighted Avg | 0.80   | 0.78   | 0.78     | 216     |

----

#### Script de entrenamiento personalizado (train.py)

##### Script de Entrenamiento de Modelos SVM y GBM

Este script de Python utiliza argparse para entrenar modelos SVM y GBM con datos de entrada especificados por el usuario.

##### Uso

1. **Estructura de Carpeta**: El script crea una carpeta con un ID aleatorio para almacenar los modelos y los informes de clasificación. Dentro de esta carpeta, se crean dos subcarpetas: `models` y `evaluation`.

2. **Argumentos de la Línea de Comandos**:

    - `--model`: Especifica el modelo a entrenar (`svm` o `gbm`).
    - `--data-file`: Ruta al archivo de datos CSV.

    Ejemplo de uso:
    ```bash
    python train_models.py --model svm --data-file data.csv
    ```

3. **Entrenamiento del Modelo SVM**:

    - Entrena un modelo de SVM con los parámetros predefinidos (`C=1`, `gamma=0.01`, `kernel='linear'`).
    - Evalúa el modelo en el conjunto de prueba.
    - Guarda el modelo SVM en la carpeta `models` y el informe de clasificación en la carpeta `evaluation`.

4. **Entrenamiento del Modelo GBM**:

    - Codifica las etiquetas usando `LabelEncoder`.
    - Crea datasets de LightGBM.
    - Entrena un modelo GBM con parámetros predefinidos.
    - Evalúa el modelo en el conjunto de prueba.
    - Guarda el modelo GBM en la carpeta `models` y el informe de clasificación en la carpeta `evaluation`.

##### Ejemplo de Estructura de Carpeta Generada

- `random_folder_id/`: Carpeta principal con un ID aleatorio que se genera automáticamente.

  - `models/`: Subcarpeta que contiene los modelos entrenados.

    - `svm_model.joblib`: Archivo que almacena el modelo SVM entrenado utilizando la biblioteca joblib.

    - `gbm_model.txt`: Archivo que guarda el modelo GBM entrenado utilizando la biblioteca LightGBM.

  - `evaluation/`: Subcarpeta que contiene informes de evaluación.

    - `classification_report.txt`: Archivo de texto que contiene el informe de clasificación generado durante la evaluación de los modelos.