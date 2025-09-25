import logging
import pandas as pd

logging.basicConfig(filename="logs/pipeline.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

df = pd.read_csv("data/raw/customers.csv")
logging.info(f"Dataset cargado con {df.shape[0]} filas y {df.shape[1]} columnas")
