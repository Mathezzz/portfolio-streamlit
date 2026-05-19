# -*- coding: utf-8 -*-
import streamlit as st
import streamlit_shadcn_ui as ui
from PIL import Image, ImageOps

from portfolio.project_data import PROJECTS
from portfolio.ui_components import (
    apply_theme,
    render_page_hero,
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

apply_theme()

# ── Mapa de ícones e chips por categoria ──────────────────────────────────────
CATEGORY_ICON = {
    "IA": "🤖",
    "BI": "📊",
    "Dados": "🔢",
    "Automação": "⚙️",
}

CATEGORY_CHIP = {
    "IA": "chip-ia",
    "BI": "chip-bi",
    "Dados": "chip-dados",
    "Automação": "chip-automacao",
}


# ── Helpers ───────────────────────────────────────────────────────────────────
def _project_categories(project: dict) -> list[str]:
    """Retorna a lista de categorias do projeto (suporta campo legado)."""
    return project.get("categorias") or [project["categoria"]]


def filter_projects(projects: list[dict], category: str, query: str) -> list[dict]:
    result = projects
    if category and category != "Todos":
        result = [p for p in result if category in _project_categories(p)]
    q = query.strip().lower()
    if q:
        result = [
            p for p in result
            if q in p["nome"].lower()
            or q in p["resumo"].lower()
            or any(q in s.lower() for s in p["stack"])
        ]
    return result


# ── Cache de imagem com fallback ──────────────────────────────────────────────
@st.cache_data(ttl=3600)
def _load_cover(path: str) -> Image.Image:
    try:
        img = Image.open(path).convert("RGB")
    except FileNotFoundError:
        img = Image.new("RGB", (1200, 700), color=(30, 41, 59))
    return ImageOps.fit(img, (1200, 700), method=Image.Resampling.LANCZOS)


# ── Hero ──────────────────────────────────────────────────────────────────────
render_page_hero(
    "Portfólio de Projetos",
    "Projetos de dados, IA e automação aplicados a desafios reais",
    "Dashboards, modelos preditivos e automações com foco em resultado e qualidade de entrega.",
)

# ── Stats rápidas ─────────────────────────────────────────────────────────────
all_categories = sorted({cat for p in PROJECTS for cat in _project_categories(p)})
all_stacks = {tech for p in PROJECTS for tech in p["stack"]}

s1, s2, s3 = st.columns(3)
s1.metric("Projetos", len(PROJECTS))
s2.metric("Categorias", len(all_categories))
s3.metric("Tecnologias", f"{len(all_stacks)}+")

st.markdown("---")

# ── Filtro e busca ────────────────────────────────────────────────────────────
render_section_title("Explorar projetos")

tab_options = ["Todos"] + all_categories
selected_category = ui.tabs(
    options=tab_options,
    default_value="Todos",
    key="project_category_tabs",
)

search_query = st.text_input(
    "Buscar projeto",
    placeholder="Nome, tecnologia ou área...",
    label_visibility="collapsed",
)

filtered = filter_projects(PROJECTS, selected_category or "Todos", search_query)


# ── Card de projeto ───────────────────────────────────────────────────────────
def render_project_card(project: dict) -> None:
    cats = _project_categories(project)
    primary_cat = project["categoria"]

    chips_html = "".join(
        f'<span class="project-meta-chip {CATEGORY_CHIP.get(c, "chip-status")}">'
        f'{CATEGORY_ICON.get(c, "📁")}&nbsp;{c}</span>'
        for c in cats
    )

    with st.container(border=True):
        st.image(_load_cover(project["imagem"]), use_container_width=True)

        st.markdown(
            f"""
            <div class="project-meta-row">
                {chips_html}
                <span class="project-meta-chip chip-status">{project['status']}</span>
                <span class="project-meta-chip chip-year">{project['ano']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<p class='project-name'>{project['nome']}</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<p class='project-summary'>{project['resumo']}</p>",
            unsafe_allow_html=True,
        )

        render_stack_badges(project["stack"], key_prefix=project["id"])

        st.markdown("<br>", unsafe_allow_html=True)

        with st.expander("Ver detalhes do projeto"):
            st.markdown(
                f"""
                <div class="detail-grid">
                    <div class="detail-cell">
                        <div class="detail-label">Objetivo</div>
                        <div class="detail-text">{project['objetivo']}</div>
                    </div>
                    <div class="detail-cell">
                        <div class="detail-label">Solução</div>
                        <div class="detail-text">{project['solucao']}</div>
                    </div>
                    <div class="detail-cell">
                        <div class="detail-label">Resultado</div>
                        <div class="detail-text">{project['resultado']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if project.get("impacto"):
                st.markdown(
                    f"""
                    <div class="impact-banner">
                        <strong>Impacto:</strong> {project['impacto']}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        render_project_actions(project["links"], project["id"])


# ── Grid de projetos ──────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

if not filtered:
    st.info("Nenhum projeto encontrado com os filtros atuais.")
else:
    col_left, col_right = st.columns(2, gap="medium")
    for i, project in enumerate(filtered):
        with col_left if i % 2 == 0 else col_right:
            render_project_card(project)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown("---")
render_section_title("Vamos conversar?")

cta_1, cta_2, cta_3 = st.columns(3)
with cta_1:
    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/anderson-matheuzzz",
        use_container_width=True,
    )
with cta_2:
    st.link_button(
        "GitHub",
        "https://github.com/Mathezzz",
        use_container_width=True,
    )
with cta_3:
    st.link_button(
        "WhatsApp",
        "https://wa.me/5584998409265?text=Ola%2C+vi+seu+portfolio+de+dados+e+quero+conversar+sobre+projetos.",
        use_container_width=True,
    )
