import logging
import pandas as pd

logging.basicConfig(filename="logs/pipeline.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

df = pd.read_csv("data/raw/customers.csv")
logging.info(f"Filas iniciales: {df.shape[0]}")

df = df.dropna(subset=["edad"])
logging.info(f"Filas después de eliminar nulos en 'edad': {df.shape[0]}")

df["edad"] = df["edad"].astype(int)
logging.info("Columna 'edad' convertida a entero")

df.to_csv("data/processed/customers_clean.csv", index=False)
logging.info("Dataset guardado en data/processed/customers_clean.csv")
