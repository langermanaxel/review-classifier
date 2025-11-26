import streamlit as st
import sys
import os

# --- FIX IMPORT ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from model.predict import predict_sentiment
# ------------------

st.title("Clasificador de Reseñas del Café ☕")
st.write("Ingresá un comentario y te digo si es positivo o negativo.")

user_input = st.text_area("Comentario:", height=120)

if st.button("Clasificar"):
    if not user_input.strip():
        st.warning("Escribí un comentario primero.")
    else:
        label, confidence = predict_sentiment(user_input)
        if label == "pos":
            st.success(f"Resultado: **POSITIVO** ({confidence:.2f} de confianza)")
        else:
            st.error(f"Resultado: **NEGATIVO** ({confidence:.2f} de confianza)")
