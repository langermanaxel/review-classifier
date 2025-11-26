# ☕ Review Classifier — NLP + Machine Learning + Dashboard 📈  
**Clasificador de reseñas para cafeterías**, desarrollado con **Python, scikit-learn, NLP y Streamlit**, capaz de analizar comentarios de clientes y determinar si son *positivos* o *negativos*.  
Incluye un **dashboard interactivo** con métricas, nubes de palabras y tendencia temporal.

---

## 🚀 Tecnologías principales

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-nltk-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data-black?logo=pandas)
![ML Project](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🎯 Objetivo del proyecto

Este proyecto permite:

- Clasificar reseñas de clientes (*positivas* o *negativas*)
- Entrenar y guardar un modelo de Machine Learning
- Analizar el sentimiento general de un negocio
- Visualizar métricas en un **dashboard profesional**
- Generar nubes de palabras según sentimiento
- Revisar tendencias temporales de comentarios
- Exportar reseñas filtradas a CSV

Ideal para:

✔ Cafeterías  
✔ Restaurantes  
✔ Tiendas de atención al cliente  
✔ Proyectos de portfolio que quieran mostrar ML + Web UI

---

## 🧠 Cómo funciona

### 🔎 1. Preprocesamiento  
Se utiliza `TfidfVectorizer` con stopwords en español (NLTK).  
Esto convierte el texto en vectores numéricos para que el modelo pueda aprender.

### 🤖 2. Modelo de Machine Learning  
El modelo utilizado es **Multinomial Naive Bayes**, uno de los más usados para análisis de texto:

- Simple, rápido y eficiente  
- Excelente para clasificación de sentimientos  
- Funciona perfecto con TF-IDF  

### 📦 3. Guardado del modelo  
El pipeline completo se guarda en:

model/model.pkl


### 🖥️ 4. App Web  
Desarrollada con **Streamlit**, incluye:

- Clasificador interactivo  
- Dashboard con métricas  
- WordCloud  
- Exportación de datos  

---

## 📁 Estructura del proyecto



review-classifier/
│
├── app/
│ ├── app.py # Clasificador con interfaz
│ └── dashboard.py # Dashboard avanzado
│
├── model/
│ ├── train.py # Entrenamiento ML
│ ├── predict.py # Función predictiva
│ └── model.pkl # Modelo entrenado
│
├── data/
│ └── reviews.csv # Dataset de reseñas
│
├── requirements.txt
└── README.md


---

## ⚙️ Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/review-classifier
cd review-classifier

2. Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate # Linux/Mac

3. Instalar dependencias
pip install -r requirements.txt

4. Entrenar el modelo
python model/train.py


Esto genera el archivo model.pkl.

5. Ejecutar el clasificador
streamlit run app/app.py


👉 Abre la app en: http://localhost:8501

6. Ejecutar el dashboard
streamlit run app/dashboard.py

🖼️ Capturas de pantalla (sugeridas)

🔍 Clasificador de reseñas

📈 Dashboard — Métricas generales

☁ Nube de palabras

📦 Dataset

El proyecto incluye un dataset inicial en:

data/reviews.csv

🧑‍💻 Autor

Axel Langerman
Desarrollador Backend & Machine Learning
📍 Río Gallegos, Argentina

🟦 LinkedIn: https://www.linkedin.com/in/axel-langerman

🐍 GitHub: https://github.com/langermanaxel

“Aprendiendo, construyendo y creciendo un proyecto a la vez.”

📝 Licencia

MIT License – Libre para usar, mejorar y compartir.


---