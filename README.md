# 🛡️ Detección de Fraude en Transacciones (sprint 2)

Proyecto de investigación (Maestría en IA – UNI) para entrenar un modelo de IA que identifique transacciones fraudulentas en tarjetas de crédito. 

Este es un ejemplo para que los alumnos lo usen como guía para organizar su repositorio.

Este repositorio forma parte del curso **Proyecto de Investigación II (MIA 403)**.

Se han añadido artefactos **didácticos** para simular el **segundo sprint** del proyecto (coherente con Semana 4–6):
- **EDA iterativo** con enfoque en decisiones (accionables).
- **Feature Engineering** básico (numéricas, categóricas y temporales si aplica).
- **Validación** correcta (Stratified K-Fold o TimeSeriesSplit) y registro de **experimentos**.

---

## 👥 Autores
- Juan Pérez – [@juanperez01](https://github.com/juanperez01)
- María Gómez – [@mariagomez02](https://github.com/mariagomez02)

---

## 📊 Dataset
- **Fuente**: [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- **Registros**: 284,807 transacciones  
- **Variables**: monto, hora, 28 features numéricos anonimizados, variable `fraude` (0/1)  
- **Versión usada**: descargada el 20/09/2025  
- **Hash** (SHA256): `3f2a1b9d7c9...`  

---

## 🗂️ Estructura del repositorio
## Nuevos/actualizados (respecto a `main`)
```
notebooks/
├── EDA_iteracion_sem4.ipynb
└── Experimentos_sem5_resultados.ipynb
src/
├── features_pipeline.py
├── modelo_iteracion.py
└── validacion.py
config/
└── experimentos.yaml
logs/
├── metrics_experimentos_template.csv
└── README_logs.md
docs/
└── HOWTO-branch-version-02.md
data/processed/
└── sample_processed.csv (muestra pequeña sintética para probar pipelines)
```
**Nota**: Los notebooks y scripts están diseñados para correr con el dataset real del repo (`data/raw/...`). La muestra `sample_processed.csv` sirve para validar el pipeline sin descargar el dataset completo.

## Métrica central
- **Clasificación**: F1 (clase positiva) + PR-AUC.
- Semillas/splits fijos, pipelines sin fuga (**fit solo en train**).
```

## ⚙️ Requisitos
Instalar dependencias usando [Poetry](https://python-poetry.org/):  
```bash
poetry install
```
O con `pip`:  
```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar el pipeline
1. **Ingesta de datos**  
   ```bash
   python src/ingesta.py
   ```
   - Carga dataset desde `data/raw/`.

2. **Preprocesamiento**  
   ```bash
   python src/preprocesamiento.py
   ```
   - Limpieza de nulos, normalización de variables.  
   - Guardado en `data/processed/`.

3. **Exploración inicial**  
   - Abrir y ejecutar el notebook `notebooks/EDA_basico.ipynb`.

4. **Entrenamiento baseline (Dummy / kNN / Naive Bayes)**
   - Opción A (script): 
   ```bash
   python src/modelo_baseline.py
   ```
   - Opción B (notebook):  
     - Abrir y ejecutar `notebooks/Baseline_basico.ipynb`  
   - Ambos generan resultados en `logs/metrics_baseline.txt`

---

## 📈 Resultados esperados (Semana 3)
- **EDA inicial** en `notebooks/EDA_basico.ipynb`.  
- **Baseline Dummy** (majority class) → Accuracy ≈ 0.99 pero sin detección de fraude.  
- **Baseline kNN (k=5)** → mejora en Recall para clase “fraude”.  
- **Métrica central**: F1-score sobre clase positiva (`fraude`).  
- **Logs de resultados** → `logs/metrics_baseline.txt`.  
- **Slides de resultados** → generados con `src/crear_slide_resultados.py` o manualmente en `slides/`.  
---

## 📌 Roadmap
- [x] Semana 2 → Ingesta + Preprocesamiento + Logging.  
- [x] Semana 3 → EDA + Baseline + Demo interna.  
- [ ] Semana 4 → Iteración con features avanzadas.  

---

## 📜 Licencia
Uso académico – Universidad Nacional de Ingeniería (UNI).
