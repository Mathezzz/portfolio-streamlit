# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 14:44:50 2025

@author: ander
"""

import streamlit as st
from PIL import Image
import base64

# ========== Configuração da Página ==========
st.set_page_config(
    page_title="Portfólio - Anderson Matheus",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ========== Carregar Imagem ==========
img = Image.open("assets/anderson_foto.jpg")

# ========== Estilo CSS opcional ==========
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ========== Header: Foto e Apresentação ==========
col1, col2 = st.columns([1, 3])

with col1:
    st.image(img, width=200)

with col2:
    st.title("Anderson Matheus")
    st.subheader("Analista de Dados | Especialista em Data Science | Foco em resolução de problemas com otimização e simulação")
    st.markdown(
        """
        Sou Analista de Dados trabalhando no setor de Franquias e Cientista de Dados, com uma paixão por Inteligência Artificial, Machine Learning e Automação de Processos. 
        Minha trajetória acadêmica inclui:
        * Bacharelado em Ciência e Tecnologia pela UFERSA (🎓)
        * Graduação em Engenharia de Produção (Em andamento)
        * Pós-Graduação em Ciência de Dados (🎓).

        Ao longo da minha carreira, desenvolvi soluções utilizando Visão Computacional e Deep Learning para análise de imagens agrícolas, focando na classificação de doenças em plantas. Tenho experiência prática com frameworks como TensorFlow e Keras, aplicando técnicas de Machine Learning para resolver problemas e extrair insights.

        Sou fascinado por como a tecnologia e a matemática computacional podem transformar dados em soluções reais. Esse interesse me inspirou a criar a newsletter "Uma Pitada de Dados", onde compartilho conhecimentos sobre Ciência de Dados, Visão Computacional e Inteligência Artificial, com o objetivo de capacitar e inspirar outros profissionais na área.
        """
    )

# ========== Links Importantes ==========
st.markdown("---")
st.markdown("📌 **Onde você pode me encontrar:**")

col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/anderson-matheuzzz")
with col2:
    st.link_button("GitHub", "https://github.com/Mathezzz")
with col3:
    st.link_button("Newsletter", "https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7202653532963934210")


# ========== Cards com Resumo ==========
st.markdown("---")
st.markdown("🧩 **Resumo das minhas habilidades:**")

card1, card2, card3 = st.columns(3)
with card1:
    st.metric("📁 Projetos", "12+", "Em diversas áreas")
with card2:
    st.metric("⚙️ Ferramentas", "Python, Power BI, SQL", "e mais...")
with card3:
    st.metric("📊 Experiência", "2+ anos", "Em dados e IA")

# ========== Botão para baixar o CV ==========
st.markdown("---")
with open("static/Curriculo Anderson Matheus.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Baixar meu CV",
    data=PDFbyte,
    file_name="CV_Anderson_Matheus.pdf",
    mime="application/pdf",
)

st.markdown("---")
st.caption("Planejando links dos projetos abaixo")
