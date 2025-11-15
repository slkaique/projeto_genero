import streamlit as st
import sqlite3
from datetime import datetime
import unicodedata

def normalizar(texto):
    if not isinstance(texto, str):
        return texto
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII','ignore').decode('utf-8')
    return texto

def inserir_denuncia():
    conn = sqlite3.connect("denuncias.db")
    cursor = conn.cursor()

    data_formatada = st.session_state.data_acontecimento.strftime("%d-%m-%Y")

    cursor.execute("""
        INSERT INTO denuncias (data_ocorrencia, data_acontecimento, setor_acontecimento, relato)
        VALUES (?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        data_formatada,
        normalizar(st.session_state.setor),
        normalizar(st.session_state.relato)
    ))

    conn.commit()
    conn.close()

    # LIMPA OS CAMPOS VIA SESSION_STATE
    st.session_state.setor = ""
    st.session_state.relato = ""
    st.session_state.data_acontecimento = datetime.now().date()

# ---------------------------------------------------------

st.title("Formulário Anônimo de Denúncia")

st.date_input("Data do acontecimento", key="data_acontecimento")
st.text_input("Setor do acontecimento", key="setor")
st.text_area("Relato da denúncia", key="relato")

st.button("Enviar denúncia", on_click=inserir_denuncia)

