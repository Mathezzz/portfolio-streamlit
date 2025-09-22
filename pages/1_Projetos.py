# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 15:26:25 2025

@author: ander
"""

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os, json

st.set_page_config(
    page_title="Projetos - Anderson",
    page_icon="🎲",
    layout="wide",
)
st.logo("assets/anderson_foto.jpg", size="large", link="https://www.linkedin.com/in/anderson-matheuzzz")


@st.cache_data(ttl=600)
def carregar_dados_sheet():
    # Carregar JSON a partir dos secrets
    if "GCP_SERVICE_ACCOUNT" in os.environ:
        service_account_info = json.loads(os.environ["GCP_SERVICE_ACCOUNT"])
    else:
        service_account_info = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info, scopes=[
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ])
    
    client = gspread.authorize(creds)
    sheet = client.open("avaliacoes-portfolio").worksheet("avaliacao")
    df = pd.DataFrame(sheet.get_all_records())
    return df

def enviar_avaliacao(projeto, nota, comentario):
    # Carregar JSON a partir dos secrets
    if "GCP_SERVICE_ACCOUNT" in os.environ:
        service_account_info = json.loads(os.environ["GCP_SERVICE_ACCOUNT"])
    else:
        service_account_info = st.secrets["gcp_service_account"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info, scopes=[
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ])
    
    client = gspread.authorize(creds)
    sheet = client.open("avaliacoes-portfolio").worksheet("avaliacao")

    # Montar nova linha (pode adicionar mais colunas se quiser, como timestamp)
    nova_linha = [str(pd.Timestamp.now()), projeto, nota, comentario]
    
    # Enviar para a planilha
    sheet.append_row(nova_linha)


def grafico_avaliacoes(projeto, df_avaliacoes):
    # Filtrar apenas o projeto desejado
    df_filtrado = df_avaliacoes[df_avaliacoes["Projeto"] == projeto]

    if df_filtrado.empty:
        st.warning("Ainda não há avaliações para este projeto.")
        return

    # Contar quantidade de cada nota
    contagem_notas = df_filtrado["Nota"].value_counts().sort_index()

    # Calcular média
    media = df_filtrado["Nota"].mean()

    # Mostrar gráfico de barras nativo do Streamlit
    st.bar_chart(contagem_notas)

    # Exibir a média em destaque
    st.markdown(f"**Média das avaliações:** ⭐ {media:.2f}")

df_avaliacao = carregar_dados_sheet()

st.title("📁 Projetos em Destaque")
st.markdown("Aqui você encontra alguns dos projetos que desenvolvi com foco em dados, IA e automação.")

# ========== Criação da galeria ==========
col1, col2 = st.columns([0.7, 0.3])


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
    nota = st.slider("Nota para o projeto (0 a 5):", 0, 5, 3)
    comentario = st.text_area("Deixe seu comentário:")
    if st.button("Enviar avaliação"):
        enviar_avaliacao("visao-tomate", nota, comentario)
        st.success("Obrigado! Sua avaliação foi registrada.")
        
    # Mostrar feedbacks anteriores
    grafico_avaliacoes("visao-tomate", df_avaliacao)
    if st.checkbox("Mostrar feedbacks anteriores"):
        st.dataframe(df_avaliacao['Comentário'])

st.markdown("---")

col3, col4 = st.columns([0.7, 0.3]) 
with col3:
    st.image("assets/dashboard-clima.png")
    st.link_button("Visualizar Dashboard", "https://lookerstudio.google.com/reporting/ec367570-1f32-4d6d-b524-f2aac68f1700")
    with st.expander("Detalhes do Dashboard"):
        st.markdown("""
                    Dashboard de análise climática.
                    
                    Dados adquiridos utilizando AppScript e OpenWheather
                    Dashboard inicialmente no Streamlit e migrado para Looker Studio
                    pelo visual e para manter a acessibilidade mais fácil.
                    """)
with col4:
    projeto = "dashboard-clima"
    nota = st.slider(f"Nota para o projeto {projeto} (0 a 5):", 0, 5, 3)
    # Campo de comentário
    comentario = st.text_area(f"Deixe seu comentário do {projeto}:")   

    if st.button("Enviar avaliação", key=f"botao_{projeto}"):
        enviar_avaliacao(projeto, nota, comentario)
        st.success("Obrigado! Sua avaliação foi registrada.")
    
    grafico_avaliacoes(projeto, df_avaliacao)
    
    if st.checkbox(f"Mostrar feedbacks anteriores de {projeto}", key=f"checkbox_{projeto}"):
        st.dataframe(df_avaliacao[df_avaliacao["projeto"] == projeto][['Comentário', 'nota']])

st.markdown("---")

col5, col6 = st.columns([0.7, 0.3])
with col5:
    st.image("assets/prototipo-petcare-hackatruck.jpg")
    st.link_button("Visualizar publicação sobre projeto", "https://www.linkedin.com/posts/anderson-matheuzzz_swiftui-swiftui-ibm-activity-7128504026186362880-LGio?utm_source=share&utm_medium=member_desktop&rcm=ACoAACrGKFkBn4uFaNxzcWuo-YFOb2BM-J2Vflg")
    with st.expander("Detalhes sobre o projeto"):
        st.markdown("""
                - **Objetivo**:Desenvolver uma solução tecnológica para apoiar animais em situação de rua, utilizando um sistema inteligente de comedouros automatizados, integrados a um aplicativo mobile. O projeto visa facilitar o cuidado, a visualização e a adoção desses animais, além de contribuir com dados para políticas públicas de saúde animal.
                - **Tecnologias**: OpenCV, IoT (Raspberry PI, câmera, sensor de presença, motor), IBM Cloudant, SwiftUI
                - **Destaques**: Cadastro Automático de Animais: Imagens captadas pelos sensores alimentam um banco de dados para registro e acompanhamento.
                """)
with col6:
    projeto = "petcare"
    nota = st.slider(f"Nota para o projeto {projeto} (0 a 5):", 0, 5, 3)
    # Campo de comentário
    comentario = st.text_area(f"Deixe seu comentário do {projeto}:")   

    if st.button("Enviar avaliação", key=f"botao_{projeto}"):
        enviar_avaliacao(projeto, nota, comentario)
        st.success("Obrigado! Sua avaliação foi registrada.")
    
    grafico_avaliacoes(projeto, df_avaliacao)
    
    if st.checkbox(f"Mostrar feedbacks anteriores de {projeto}", key=f"checkbox_{projeto}"):
        st.dataframe(df_avaliacao[df_avaliacao["projeto"] == projeto][['Comentário', 'nota']])
                
st.markdown("---")

col7, col8 = st.columns([0.7, 0.3])
with col7:
    st.image("assets/ocr_exemplo.png")
    st.link_button("Testar Ferramenta(Em breve)", "https://www.linkedin.com/posts/anderson-matheuzzz_analisededados-cienciadedados-ocr-activity-7322424522605772800-WA-j?utm_source=share&utm_medium=member_desktop&rcm=ACoAACrGKFkBn4uFaNxzcWuo-YFOb2BM-J2Vflg")
    with st.expander("OCR de imagens para texto"):
        st.markdown("""
        - **Objetivo**: Extrair texto a partir de imagens, com ideias para transformar prints, fotos e scans em arquivos de texto.
        - **Tecnologias**: OpenCV, PyTesseract, SciKit-Learn e Pipeline.
        - **Destaques**: Gerando texto em retorno, mas é possível também retornar o arquivo com extensão .txt.
        - Obs.: Em breve deixo a ferramenta disponível, ainda estou organizando o portfolio.
        """)

with col8:
    projeto = "ocr-texto"
    nota = st.slider(f"Nota para o projeto {projeto} (0 a 5):", 0, 5, 3)
    # Campo de comentário
    comentario = st.text_area(f"Deixe seu comentário do {projeto}:")   

    if st.button("Enviar avaliação", key=f"botao_{projeto}"):
        enviar_avaliacao(projeto, nota, comentario)
        st.success("Obrigado! Sua avaliação foi registrada.")
    
    grafico_avaliacoes(projeto, df_avaliacao)
    
    if st.checkbox(f"Mostrar feedbacks anteriores de {projeto}", key=f"checkbox_{projeto}"):
        st.dataframe(df_avaliacao[df_avaliacao["projeto"] == projeto][['Comentário', 'nota']])