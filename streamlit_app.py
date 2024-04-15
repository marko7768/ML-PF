import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

model = joblib.load('modelo_regresion.pkl')

st.title('Aplicación ML')

input_text = st.text_input('Ingrese un texto para analizar sentimientos:')

def preprocess_text(text):
    vectorizer = TfidfVectorizer()

    textVectorizado = vectorizer.fit_transform([text])
    return textVectorizado

if st.button('Analizar Sentimientos'):
    preprocessed_text = preprocess_text(input_text)
    prediction = model.predict(preprocessed_text)
    sentiment = 'Positivo' if prediction[0] == 0 else 'Negativo'
    st.write(f'El sentimiento del texto es: {sentiment}')