import streamlit as st
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import re

import nltk
nltk.download('stopwords')

model = joblib.load('modelo_regresion.pkl')

st.title('Aplicación de Regresión Lineal')

input_text = st.text_input('Ingrese un texto para analizar sentimientos:')

def preprocess_text(text):
    port_stem = PorterStemmer()
    vectorizer = TfidfVectorizer()

    stemmed_content = re.sub('[^a-zA-Z]',' ',text)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)

    textVectorizado = vectorizer.fit_transform(stemmed_content)
    return textVectorizado

if st.button('Analizar Sentimientos'):
    preprocessed_text = preprocess_text(input_text)
    prediction = model.predict(input_text)
    sentiment = 'Positivo' if prediction[0] == 1 else 'Negativo'
    st.write(f'El sentimiento del texto es: {sentiment}')