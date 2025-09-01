# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 15:26:25 2025

@author: ander
"""

import streamlit as st

st.set_page_config(page_title="Projetos - Anderson", layout="wide")
st.set_page_config(
    page_title="Projetos - Anderson",
    page_icon="🎲",
    layout="wide",
)
st.logo("assets/anderson_foto.jpg", size="large", link="https://www.linkedin.com/in/anderson-matheuzzz")

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
    st.link_button("Testar Ferramenta(Em breve)", "https://www.linkedin.com/posts/anderson-matheuzzz_analisededados-cienciadedados-ocr-activity-7322424522605772800-WA-j?utm_source=share&utm_medium=member_desktop&rcm=ACoAACrGKFkBn4uFaNxzcWuo-YFOb2BM-J2Vflg")
    with st.expander("OCR de imagens para texto"):
        st.markdown("""
        - **Objetivo**: Extrair texto a partir de imagens, com ideias para transformar prints, fotos e scans em arquivos de texto.
        - **Tecnologias**: OpenCV, PyTesseract, SciKit-Learn e Pipeline.
        - **Destaques**: Gerando texto em retorno, mas é possível também retornar o arquivo com extensão .txt.
        - Obs.: Em breve deixo a ferramenta disponível, ainda estou organizando o portfolio.
        """)
        
with col3:
    st.image("assets/prototipo-petcare-hackatruck.jpg")
    st.link_button("Visualizar publicação sobre projeto", "https://www.linkedin.com/posts/anderson-matheuzzz_swiftui-swiftui-ibm-activity-7128504026186362880-LGio?utm_source=share&utm_medium=member_desktop&rcm=ACoAACrGKFkBn4uFaNxzcWuo-YFOb2BM-J2Vflg")
    with st.expander("Detalhes sobre o projeto"):
        st.markdown("""
                - **Objetivo**:Desenvolver uma solução tecnológica para apoiar animais em situação de rua, utilizando um sistema inteligente de comedouros automatizados, integrados a um aplicativo mobile. O projeto visa facilitar o cuidado, a visualização e a adoção desses animais, além de contribuir com dados para políticas públicas de saúde animal.
                - **Tecnologias**: OpenCV, IoT (Raspberry PI, câmera, sensor de presença, motor), IBM Cloudant, SwiftUI
                - **Destaques**: Cadastro Automático de Animais: Imagens captadas pelos sensores alimentam um banco de dados para registro e acompanhamento.
                """)
                
st.markdown("---")

col4, col5, col6 = st.columns(3)
with col4:
    st.image("assets/dashboard-clima.png")
    st.link_button("Visualizar Dashboard", "https://lookerstudio.google.com/reporting/ec367570-1f32-4d6d-b524-f2aac68f1700")
    with st.expander("Detalhes do Dashboard"):
        st.markdown("""
                    Dashboard de análise climática.
                    
                    Dados adquiridos utilizando AppScript e OpenWheather
                    Dashboard inicialmente no Streamlit e migrado para Looker Studio
                    pelo visual e para manter a acessibilidade mais fácil.
                    """)
