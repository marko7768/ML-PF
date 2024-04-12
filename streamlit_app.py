import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

import nltk
nltk.download('stopwords')

model = joblib.load('modelo_regresion.pkl')

st.title('Aplicación de Regresión Lineal')

input_text = st.text_input('Ingrese un texto para analizar sentimientos:')

def preprocess_text(text):
    text_list = [text]
    #port_stem = PorterStemmer()
    vectorizer = TfidfVectorizer()
    textVectorizado = vectorizer.fit_transform(text_list)
    return textVectorizado

if st.button('Analizar Sentimientos'):
    preprocessed_text = preprocess_text(input_text)
    prediction = model.predict([preprocessed_text])
    sentiment = 'Positivo' if prediction[0] == 1 else 'Negativo'
    st.write(f'El sentimiento del texto es: {sentiment}')