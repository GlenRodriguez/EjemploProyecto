import logging
import pandas as pd

logging.basicConfig(filename="logs/pipeline.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

df = pd.read_csv("data/raw/customers.csv")
logging.info(f"Dataset cargado con {df.shape[0]} filas y {df.shape[1]} columnas")

# En proyectos de investigación chicos, se puede juntar todo en preprocesamiento.py.
# Pero en proyectos más grandes, la ingesta suele ser un paso distinto:
#     Descargar datos desde una API.
#     Consultar una base de datos SQL y bajar registros a un .csv.
#     Bajar datos de Kaggle o un FTP institucional.
#     Copiar datos crudos de un sensor, log de sistema, etc.
#     Hacer web scrapping y guardarlo a disco
# Por eso se separa → ingesta.py asegura que siempre tengas los datos crudos en data/raw/.
