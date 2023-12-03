import argparse
import os
import random
import string
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib

def generate_random_id(length=8):
    """Generar un ID aleatorio."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def train_svm(X_train, y_train, X_test, y_test, output_dir):
    # Entrenar el modelo SVM con los parámetros dados
    svm_model = SVC(C=1, gamma=0.01, kernel='linear')
    svm_model.fit(X_train, y_train)

    # Hacer predicciones y evaluar el rendimiento
    y_pred = svm_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy SVM: {accuracy}")

    # Guardar el modelo
    model_path = os.path.join(output_dir, "models", "svm_model.joblib")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(svm_model, model_path)

    # Guardar el informe de clasificación
    evaluation_path = os.path.join(output_dir, "evaluation", "classification_report.txt")
    os.makedirs(os.path.dirname(evaluation_path), exist_ok=True)
    with open(evaluation_path, "w") as f:
        f.write(classification_report(y_test, y_pred))
    print(f"Informe de clasificación guardado en: {evaluation_path}")

def train_gbm(X_train, y_train, X_test, y_test, output_dir):
    # Codificar las etiquetas usando LabelEncoder
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    y_test_encoded = label_encoder.transform(y_test)

    # Crear datasets de LightGBM
    lgb_train = lgb.Dataset(X_train, y_train_encoded)
    lgb_test = lgb.Dataset(X_test, y_test_encoded)

    # Configurar parámetros y entrenar el modelo GBM
    params = {
        'task': 'train',
        'boosting_type': 'gbdt',
        'objective': 'multiclass',
        'num_class': 27,
        'metric': 'multi_logloss'
    }
    gbm = lgb.train(params, lgb_train, num_boost_round=150, valid_sets=[lgb_test])

    # Guardar el modelo
    model_path = os.path.join(output_dir, "models", "gbm_model.txt")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    gbm.save_model(model_path)

    # Guardar el informe de clasificación
    predictions = gbm.predict(X_test)
    predicted_classes = np.argmax(predictions, axis=1)
    evaluation_path = os.path.join(output_dir, "evaluation", "classification_report.txt")
    os.makedirs(os.path.dirname(evaluation_path), exist_ok=True)
    with open(evaluation_path, "w") as f:
        f.write(classification_report(y_test_encoded, predicted_classes))
    print(f"Informe de clasificación guardado en: {evaluation_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entrenamiento de modelos SVM y GBM.")
    parser.add_argument("--model", choices=["svm", "gbm"], help="Especifica el modelo a entrenar (svm, gbm)", required=True)
    parser.add_argument("--data-file", help="Ruta al archivo de datos CSV", required=True)

    args = parser.parse_args()

    # Crear una carpeta con ID aleatorio
    output_dir = generate_random_id()
    os.makedirs(output_dir, exist_ok=True)

    # Cargar datos desde el archivo CSV
    data = pd.read_csv(args.data_file)
    X = data.drop(columns=['label'])
    y = data['label']

    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Verificar qué modelo entrenar
    if args.model == "svm":
        train_svm(X_train, y_train, X_test, y_test, output_dir)
    elif args.model == "gbm":
        train_gbm(X_train, y_train, X_test, y_test, output_dir)
    else:
        print("Modelo no reconocido. Por favor, elija 'svm' o 'gbm'.")