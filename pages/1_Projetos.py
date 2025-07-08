# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 15:26:25 2025

@author: ander
"""

import streamlit as st

st.set_page_config(page_title="Projetos - Anderson", layout="wide")

st.title("📁 Projetos em Destaque")
st.markdown("Aqui você encontra alguns dos projetos que desenvolvi com foco em dados, IA e automação.")

# ========== Criação da galeria ==========
col1, col2, col3 = st.columns(3)


# Projeto tomate
with col1:
    st.image("assets/tomate_exemplo.png", use_container_width=True)
    st.link_button("Ver no GitHub", "https://www.linkedin.com/posts/anderson-matheuzzz_cienciadedados-analisededados-redesneurais-activity-7348087036395843585-p2hs?utm_source=share&utm_medium=member_desktop&rcm=ACoAACrGKFkBn4uFaNxzcWuo-YFOb2BM-J2Vflg")
    with st.expander("🔍 Detecção de tomates com Visão Computacional"):
        st.markdown("""
        - **Objetivo**: Auxiliar no processo de seleção e inspeção de qualidade de tomates, reduzindo erros humanos.
        - **Tecnologias**: OpenCV, Keras, CNNs, Streamlit.
        - **Destaques**: Aplicação baseada em um projeto do livro 'Redes Neurais Artificiais' do Prof. Ivan N.
        - Obs.: Em breve deixo a ferramenta disponível, ainda estou organizando o portfolio.
        """)
        
with col2:
    st.image("assets/ocr_exemplo.png")
    st.link_button("Testar Ferramenta", "https://www.linkedin.com/posts/anderson-matheuzzz_analisededados-cienciadedados-ocr-activity-7322424522605772800-WA-j?utm_source=share&utm_medium=member_desktop&rcm=ACoAACrGKFkBn4uFaNxzcWuo-YFOb2BM-J2Vflg")
    with st.expander("OCR de imagens para texto"):
        st.markdown("""
        - **Objetivo**: Extrair texto a partir de imagens, com ideias para transformar prints, fotos e scans em arquivos de texto.
        - **Tecnologias**: OpenCV, PyTesseract, SciKit-Learn e Pipeline.
        - **Destaques**: Gerando texto em retorno, mas é possível também retornar o arquivo com extensão .txt.
        - Obs.: Em breve deixo a ferramenta disponível, ainda estou organizando o portfolio.
        """)