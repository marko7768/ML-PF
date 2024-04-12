import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk import WordNetLemmatizer
import joblib

import nltk
nltk.download('stopwords')

model = joblib.load('modelo_regresion.pkl')

st.title('Aplicación de Regresión Lineal')

input_text = st.text_input('Ingrese un texto para analizar sentimientos:')

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return ' '.join(lemmatized_tokens)

if st.button('Analizar Sentimientos'):
    preprocessed_text = preprocess_text(input_text)
    prediction = model.predict([preprocessed_text])
    sentiment = 'Positivo' if prediction[0] == 1 else 'Negativo'
    st.write(f'El sentimiento del texto es: {sentiment}')