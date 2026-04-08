# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 11:17:38 2025

@author: ander
"""

import streamlit as st
import streamlit_shadcn_ui as ui

from portfolio.ui_components import (
    apply_theme,
    close_soft_panel,
    open_soft_panel,
    render_page_hero,
    render_section_title,
)

st.set_page_config(
    page_title="Projetos - Anderson",
    page_icon="👤",
    layout="wide",
)
apply_theme()
st.logo("assets/anderson_foto.jpg", size="large", link="https://www.linkedin.com/in/anderson-matheuzzz")

render_page_hero(
    "Sobre Mim",
    "Trajetoria profissional e academica",
    "Uma visao cronologica da minha evolucao em tecnologia, dados e lideranca de projetos.",
)

ui.badges(
    badge_list=[("Engenharia", "secondary"), ("Dados", "default"), ("Negocios", "secondary")],
    key="about_badges",
)

# ========== Criação dos espaços para storytelling ==========
col1, col2 = st.columns(2)
with col1:
    open_soft_panel()
    render_section_title("Inicio da jornada")
    st.markdown("""
                Minha trajetória profissional começou ainda no ensino médio, quando cursei o técnico em Eletrotécnica. 
                Foi ali que tive meu primeiro contato com automação e programação, por meio da disciplina de Automação Industrial, 
                utilizando linguagem Ladder e blocos funcionais com o software LOGO! da Siemens. 
                Essa base prática despertou em mim um interesse profundo por sistemas automatizados e 
                pelo potencial da tecnologia na resolução de problemas reais.
                
                Simultaneamente, durante o curso técnico, estagiei na industria Itapetinga Agro Industrial, produtora do cimento NASSAU,
                 onde pude ver como era a rotina de manutenções, os planejamentos necessários para a equipe, recursos e etc.
                Conhecimento e experiência que mais para frente fez muita diferença no meu pensamento crítico na graduação de Engenharia de Produção.
                """)
    close_soft_panel()
                
with col2:
    st.image("assets/forno-itapetinga-painel.png")

st.markdown("---")

col3, col4 = st.columns(2)
with col3:
    st.image("assets/eu-faco-robos-obr.jpg")
                
with col4:  
    open_soft_panel()
    render_section_title("Formacao e lideranca")
    st.markdown("""
                Buscando expandir meus conhecimentos, ingressei no Bacharelado em Ciência e Tecnologia, 
                onde aprofundei meus estudos em matemática, física e outras ciências exatas, além de desenvolver 
                habilidades em programação com linguagens como Java, Python, MATLAB e R. 
                
                Durante esse período, atuei como monitor em um projeto de extensão de Robótica Educacional, 
                onde fui responsável pela elaboração dos planos de aula, integração da robótica com outras disciplinas 
                do currículo escolar e também pelo ensino de conceitos mais avançados, como controle e sensores. 
                
                Sob minha orientação, a equipe de alunos que liderei conquistou o 2º lugar geral na etapa regional da 
                competição FLL (First Lego League) — destaque obtido após bom desempenho em todas as categorias. 
                Posteriormente, representamos nossa região na etapa nacional com recursos arrecadados por meio de rifas,
                eventos e vendas (de trufas e outros doces). O que gosto de pensar como minha primeira experiência gerenciando projetos,
                 já que precisamos equilibrar conhecimentos de cronogramas, custos, qualidade das entregas e escopo em si para chegarmos 
                ao resultado: O valor para levar para o Rio de Janeiro 8 alunos do Ensino Municipal de Mossoró, 
                com eles tendo a experiência pela primeira vez de andarem de avião! 🛫
                """)
    close_soft_panel()
                
st.markdown("---")

col5, col6 = st.columns(2)
with col5:
    open_soft_panel()
    render_section_title("Transicao para dados")
    st.markdown("""
                Comecei minhas primeiras experiências como Freelancer, onde me aproveitando da base matemática e estatística 
                da graduação pude desenvolver projetos de Machine Learning e análise de dados para clientes. Tive contato com 
                a área de Inteligência Artificial e Matemática Computacional em projetos práticos na faculdade, então me desenvolvi rápido nestas disciplinas.
                
                ---
                Alguns dos projetos que desenvolvi como Freelancer estão listados na área de projetos deste portfólio:
                
                """)
    st.page_link("pages/1_Projetos.py", label="Veja alguns de meus projetos", icon="👾")
    st.markdown("""
                ---
                
                Minha experiência no mercado de trabalho se consolidou na Bee Delivery, onde entrei como Analista de 
                Negócios no setor de franquias.
                
                Nessa função, trabalhei principalmente com **Power BI, Excel e Python**, 
                **utilizando os dados para gerar insights e propor planos de ação estruturados no modelo PDCA**, apoiando-me 
                também em **ferramentas clássicas de análise como SWOT e as 5 Forças de Porter**.
                
                Foi nesse período que iniciei 
                e concluí minha **pós-graduação em Data Science** 🎲🔮, o que me permitiu evoluir tecnicamente e ser promovido a 
                Analista de Dados.
                """)
    close_soft_panel()
    
with col6:
    st.image("assets/anderson-bee-reuniao-blur.png")

st.markdown("---")