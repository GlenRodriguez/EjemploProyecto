# 🛡️ Detección de Fraude en Transacciones

Proyecto de investigación (Maestría en IA – UNI) para entrenar un modelo de IA que identifique transacciones fraudulentas en tarjetas de crédito. 

Este es un ejemplo para que los alumnos lo usen como guía para organizar su repositorio.

Este repositorio forma parte del curso **Proyecto de Investigación II (MIA 403)**.

---

## 👥 Autores
- Juan Pérez – [@juanperez01](https://github.com/juanperez01)
- María Gómez – [@mariagomez02](https://github.com/mariagomez02)
- Glen Rodriguez - [@GlenRodriguez](https://github.com/GlenRodriguez)
---

## 📊 Dataset
- **Fuente**: [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- **Registros**: 284,807 transacciones  
- **Variables**: monto, hora, 28 features numéricos anonimizados, variable `fraude` (0/1)  
- **Versión usada**: descargada el 20/09/2025  
- **Hash** (SHA256): `3f2a1b9d7c9...`  

---

## 🗂️ Estructura del repositorio
```
data/
 ├── raw/          # dataset original
 ├── processed/    # dataset limpio y transformado
notebooks/         
 ├── EDA_basico.ipynb         # Análisis exploratorio inicial
 └── Baseline_basico.ipynb    # Entrenamiento de baselines (Dummy + kNN)
src/               
 ├── ingesta.py               # script de ingesta
 ├── preprocesamiento.py      # script de preprocesamiento
 └── modelo_baseline.py       # script con modelo Dummy + kNN
logs/              # archivos de logging y métricas
slides/            # presentaciones de resultados
README.md
pyproject.toml
poetry.lock / requirements.txt
.gitignore
```

---

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
