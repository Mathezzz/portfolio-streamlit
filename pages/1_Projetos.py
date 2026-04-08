import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui

from portfolio.feedback import load_feedback, save_feedback
from portfolio.project_data import PROJECTS
from portfolio.ui_components import (
    apply_theme,
    render_hero,
    render_project_actions,
    render_section_title,
    render_stack_badges,
)


st.set_page_config(page_title="Projetos - Anderson", page_icon="🎲", layout="wide")
st.logo(
    "assets/anderson_foto.jpg",
    size="large",
    link="https://www.linkedin.com/in/anderson-matheuzzz",
)


def _project_metrics(project_feedback: pd.DataFrame) -> tuple[float, int]:
    if project_feedback.empty:
        return 0.0, 0
    return float(project_feedback["Nota"].mean()), int(project_feedback.shape[0])


def _render_feedback_section(project: dict, feedback_df: pd.DataFrame, feedback_source: str) -> None:
    project_feedback = feedback_df[feedback_df["Projeto"] == project["id"]]
    avg, votes = _project_metrics(project_feedback)

    st.markdown("<div class='social-proof-box'>", unsafe_allow_html=True)
    render_section_title("Prova social")
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Media", f"{avg:.1f}" if votes else "-", f"{votes} votos")
    col_m2.metric("Status", "Online" if feedback_source == "online" else "Offline")

    if not project_feedback.empty:
        rating_count = (
            project_feedback["Nota"].value_counts().reindex(range(0, 6), fill_value=0)
        )
        st.bar_chart(rating_count)

        with st.expander("Comentarios recentes"):
            comments = project_feedback[project_feedback["Comentario"].astype(str).str.strip() != ""]
            if comments.empty:
                st.caption("Ainda nao ha comentarios com texto para este projeto.")
            else:
                st.dataframe(
                    comments[["Timestamp", "Nota", "Comentario"]]
                    .sort_values(by="Timestamp", ascending=False)
                    .head(8),
                    use_container_width=True,
                    hide_index=True,
                )

    with st.form(key=f"form_feedback_{project['id']}"):
        note = st.slider("Nota", min_value=0, max_value=5, value=4, key=f"note_{project['id']}")
        comment = st.text_area(
            "Comentario (opcional)",
            placeholder="O que voce gostou ou o que pode melhorar?",
            key=f"comment_{project['id']}",
        )
        submitted = st.form_submit_button("Enviar avaliacao")
        if submitted:
            ok, message = save_feedback(project["id"], note, comment)
            if ok:
                st.success(message)
                st.cache_data.clear()
                st.rerun()
            else:
                st.error(message)

    st.markdown("</div>", unsafe_allow_html=True)


@st.cache_data(ttl=300)
def get_feedback() -> tuple[pd.DataFrame, str]:
    return load_feedback()


def filter_projects(projects: list[dict], category: str, query: str) -> list[dict]:
    filtered = projects
    if category != "Todos":
        filtered = [project for project in filtered if project["categoria"] == category]

    q = query.strip().lower()
    if q:
        filtered = [
            project
            for project in filtered
            if q in project["nome"].lower() or q in project["resumo"].lower()
        ]
    return filtered


def render_project_card(project: dict, feedback_df: pd.DataFrame, feedback_source: str) -> None:
    with st.container(border=True):
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        st.image(project["imagem"], use_container_width=True)
        st.subheader(project["nome"])
        st.caption(f"{project['categoria']} | {project['status']} | {project['ano']}")
        st.markdown(f"<p class='project-summary'>{project['resumo']}</p>", unsafe_allow_html=True)

        render_stack_badges(project["stack"], key_prefix=project["id"])

        col_i1, col_i2 = st.columns(2)
        col_i1.metric("Impacto", project["impacto"])
        col_i2.metric("Ano", project["ano"])

        with st.expander("Detalhes"):
            st.markdown(f"**Objetivo:** {project['objetivo']}")
            st.markdown(f"**Solucao:** {project['solucao']}")
            st.markdown(f"**Resultado:** {project['resultado']}")

        render_project_actions(project["links"], project["id"])
        _render_feedback_section(project, feedback_df, feedback_source)
        st.markdown("</div>", unsafe_allow_html=True)


apply_theme()
render_hero()

feedback_df, feedback_source = get_feedback()

render_section_title("Filtrar projetos")
selected_category = ui.tabs(
    options=["Todos", "Dados", "IA", "Automacao", "BI"],
    default_value="Todos",
    key="project_category_tabs",
)
search_query = st.text_input("Buscar por nome ou resumo")

filtered_projects = filter_projects(PROJECTS, selected_category or "Todos", search_query)

if not filtered_projects:
    st.warning("Nenhum projeto encontrado com os filtros atuais.")
else:
    page_size = 2
    total_pages = max(1, (len(filtered_projects) + page_size - 1) // page_size)
    current_page = ui.pagination(
        key="projects_pagination",
        totalPages=total_pages,
        initialPage=1,
    )
    try:
        page = int(current_page)
    except (TypeError, ValueError):
        page = 1

    start = (max(1, page) - 1) * page_size
    end = start + page_size
    projects_slice = filtered_projects[start:end]

    col_left, col_right = st.columns(2)
    for index, project in enumerate(projects_slice):
        target_col = col_left if index % 2 == 0 else col_right
        with target_col:
            render_project_card(project, feedback_df, feedback_source)

st.markdown("---")
render_section_title("Vamos conversar?")
cta_1, cta_2, cta_3 = st.columns(3)
with cta_1:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/anderson-matheuzzz", use_container_width=True)
with cta_2:
    st.link_button("GitHub", "https://github.com/Mathezzz", use_container_width=True)
with cta_3:
    st.link_button(
        "WhatsApp",
        "https://wa.me/5584998409265?text=Ola%2C+vi+seu+portfolio+de+dados+e+quero+conversar+sobre+projetos.",
        use_container_width=True,
    )