import os
import logging
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    processed = Path("data/processed/customers_clean.csv")
    raw = Path("data/raw/customers.csv")
    if processed.exists():
        logging.info("Cargando dataset procesado (customers_clean.csv)")
        df = pd.read_csv(processed)
    elif raw.exists():
        logging.info("Cargando dataset crudo (customers.csv) y aplicando preprocesamiento mínimo")
        import numpy as np
        df = pd.read_csv(raw).dropna(subset=["edad"]).copy()
        df["edad"] = df["edad"].astype(int)
    else:
        raise FileNotFoundError("No se encontró data/processed/customers_clean.csv ni data/raw/customers.csv")
    return df

def main():
    df = load_data()
    X = df[["edad", "monto"]].values
    y = df["fraude"].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # Dummy
    dummy = DummyClassifier(strategy="most_frequent")
    dummy.fit(X_train, y_train)
    y_pred_dummy = dummy.predict(X_test)

    # kNN
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train_std, y_train)
    y_pred_knn = knn.predict(X_test_std)

    rep_dummy = classification_report(y_test, y_pred_dummy, digits=4)
    rep_knn = classification_report(y_test, y_pred_knn, digits=4)

    from sklearn.metrics import confusion_matrix
    cm_dummy = confusion_matrix(y_test, y_pred_dummy).tolist()
    cm_knn = confusion_matrix(y_test, y_pred_knn).tolist()

    os.makedirs("logs", exist_ok=True)
    with open("logs/metrics_baseline.txt", "w", encoding="utf-8") as f:
        f.write("=== Dummy (majority class) ===\n")
        f.write(rep_dummy + "\n")
        f.write(f"Confusion matrix: {cm_dummy}\n\n")
        f.write("=== kNN (k=5) ===\n")
        f.write(rep_knn + "\n")
        f.write(f"Confusion matrix: {cm_knn}\n")

    logging.info("Baselines entrenados. Resultados guardados en logs/metrics_baseline.txt")
    print("Listo. Revisa logs/metrics_baseline.txt")

if __name__ == "__main__":
    main()
