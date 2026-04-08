# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 14:44:50 2025

@author: ander
"""

import streamlit as st
from PIL import Image
import streamlit_shadcn_ui as ui

from portfolio.ui_components import (
    apply_theme,
    close_soft_panel,
    open_soft_panel,
    render_page_hero,
    render_section_title,
)

# ========== Configuração da Página ==========
st.set_page_config(
    page_title="Portfólio - Anderson Matheus",
    page_icon="📊",
    layout="wide",
)

apply_theme()

st.logo("assets/anderson_foto.jpg", size="large", link="https://www.linkedin.com/in/anderson-matheuzzz")

# ========== Carregar Imagem ==========
img = Image.open("assets/anderson_foto.jpg")

render_page_hero(
    "Portfolio de Dados e IA",
    "Anderson Matheus",
    "Analista de Dados e Cientista de Dados com foco em resolver problemas reais com dados, modelagem e automacao.",
)

# ========== Header: Foto e Apresentação ==========
col1, col2 = st.columns([1, 3])

with col1:
    st.image(img, width=200)

with col2:
    render_section_title("Perfil profissional")
    ui.badges(badge_list=[("Dados", "default"), ("IA", "secondary"), ("Automacao", "secondary")], key="home_badges")
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
render_section_title("Onde me encontrar")

col1, col2, col3, col4 = st.columns(4)
with col1:
    open_soft_panel()
    st.write("Me conheça um pouco mais e meus conteúdos:")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/anderson-matheuzzz")
    close_soft_panel()
with col2:
    open_soft_panel()
    st.write("Github com alguns projetos:")
    st.link_button("GitHub", "https://github.com/Mathezzz")
    close_soft_panel()
with col3:
    open_soft_panel()
    st.write("Uma pitada de dados:")
    st.image("assets/logo pitada de dados.png", width=200)
    st.link_button("Newsletter", "https://www.linkedin.com/build-relation/newsletter-follow?entityUrn=7202653532963934210")
    close_soft_panel()
with col4:
    open_soft_panel()
    st.write("Contato: (84) 9 9840-9265")
    st.link_button("Fale comigo no Whatsapp", "https://wa.me/5584998409265?text=Ol%C3%A1%2C%20vi%20seu%20portf%C3%B3lio%20de%20dados%20e%20resolvi%20entrar%20em%20contato%20com%20voc%C3%AA!")
    close_soft_panel()


# ========== Cards com Resumo ==========
st.markdown("---")
render_section_title("Resumo das minhas habilidades")

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
st.caption("Navegue pelas paginas ao lado para ver projetos e trajetoria completa.")
