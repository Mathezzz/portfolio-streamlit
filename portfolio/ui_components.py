import streamlit as st
import streamlit_shadcn_ui as ui


def apply_theme() -> None:
    st.markdown(
        """
        <style>
            .hero-shell {
                background: linear-gradient(140deg, #0f172a 0%, #1e293b 45%, #334155 100%);
                border: 1px solid rgba(148, 163, 184, 0.25);
                border-radius: 20px;
                padding: 1.3rem 1.4rem;
                margin-bottom: 1rem;
            }
            .hero-kicker {
                color: #93c5fd;
                font-size: 0.85rem;
                letter-spacing: 0.06em;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 0.35rem;
            }
            .hero-title {
                color: #f8fafc;
                font-size: 2rem;
                font-weight: 800;
                line-height: 1.1;
                margin: 0;
            }
            .hero-subtitle {
                color: #ffffff;
                margin-top: 0.5rem;
                font-size: 1rem;
            }
            .section-title {
                font-size: 1.25rem;
                font-weight: 700;
                margin: 0.6rem 0 0.2rem;
            }
            .project-card {
                border: 1px solid rgba(148, 163, 184, 0.25);
                border-radius: 16px;
                padding: 0.8rem;
                background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
            }
            .project-summary {
                color: #94a3b8;
                font-size: 0.95rem;
                margin: 0.4rem 0 0.6rem;
            }
            .social-proof-box {
                border: 1px dashed rgba(148, 163, 184, 0.45);
                border-radius: 16px;
                padding: 0.8rem 1rem;
                margin-top: 0.8rem;
            }
            .soft-panel {
                border: 1px solid rgba(148, 163, 184, 0.20);
                border-radius: 16px;
                padding: 1rem;
                background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
            }
            .text-muted {
                color: #94a3b8;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <section class='hero-shell'>
            <div class='hero-kicker'>Portfólio de Projetos</div>
            <h1 class='hero-title'>Projetos de dados, IA e automação aplicados a desafios reais</h1>
            <p class='hero-subtitle'>Aqui você encontra dashboards, modelos e automações desenvolvidos com foco em resultado e qualidade de entrega.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_page_hero(kicker: str, title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <section class='hero-shell'>
            <div class='hero-kicker'>{kicker}</div>
            <h1 class='hero-title'>{title}</h1>
            <p class='hero-subtitle'>{subtitle}</p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(text: str) -> None:
    st.markdown(f"<h2 class='section-title'>{text}</h2>", unsafe_allow_html=True)


def open_soft_panel() -> None:
    st.markdown("<div class='soft-panel'>", unsafe_allow_html=True)


def close_soft_panel() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def render_stack_badges(stacks: list[str], key_prefix: str) -> None:
    badge_list = [(item, "secondary") for item in stacks]
    ui.badges(badge_list=badge_list, key=f"{key_prefix}_stack")


def render_project_actions(links: dict, project_id: str) -> None:
    col_a, col_b = st.columns(2)
    with col_a:
        if links.get("demo"):
            st.link_button("Ver demo", links["demo"], use_container_width=True)
        elif links.get("publicacao"):
            st.link_button("Ver publicação", links["publicacao"], use_container_width=True)

    with col_b:
        if links.get("github"):
            st.link_button("Repositório", links["github"], use_container_width=True)
        else:
            st.button("Repositório em breve", key=f"{project_id}_repo_placeholder", disabled=True, use_container_width=True)
