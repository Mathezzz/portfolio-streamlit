import streamlit as st
import streamlit_shadcn_ui as ui


def apply_theme() -> None:
    st.markdown(
        """
        <meta charset="utf-8">
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
            .project-meta-row {
                display: flex;
                align-items: center;
                gap: 0.5rem;
                margin: 0.5rem 0 0.3rem;
                flex-wrap: wrap;
            }
            .project-meta-chip {
                font-size: 0.75rem;
                font-weight: 600;
                padding: 0.2rem 0.55rem;
                border-radius: 999px;
                letter-spacing: 0.03em;
            }
            .chip-ia       { background: rgba(139,92,246,0.18); color: #c4b5fd; border: 1px solid rgba(139,92,246,0.35); }
            .chip-bi       { background: rgba(16,185,129,0.15); color: #6ee7b7; border: 1px solid rgba(16,185,129,0.30); }
            .chip-dados    { background: rgba(59,130,246,0.15); color: #93c5fd; border: 1px solid rgba(59,130,246,0.30); }
            .chip-automacao{ background: rgba(245,158,11,0.15); color: #fcd34d; border: 1px solid rgba(245,158,11,0.30); }
            .chip-status   { background: rgba(148,163,184,0.10); color: #94a3b8; border: 1px solid rgba(148,163,184,0.25); }
            .chip-year     { background: transparent; color: #64748b; border: none; font-weight: 500; }
            .project-name {
                font-size: 1.15rem;
                font-weight: 700;
                line-height: 1.3;
                margin: 0.2rem 0 0.1rem;
            }
            .project-summary {
                color: #94a3b8;
                font-size: 0.92rem;
                margin: 0.3rem 0 0.6rem;
                line-height: 1.5;
            }
            .detail-grid {
                display: grid;
                grid-template-columns: 1fr 1fr 1fr;
                gap: 0.6rem;
                margin-top: 0.4rem;
            }
            .detail-cell {
                background: rgba(255,255,255,0.03);
                border: 1px solid rgba(148,163,184,0.15);
                border-radius: 10px;
                padding: 0.6rem 0.7rem;
            }
            .detail-label {
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.07em;
                text-transform: uppercase;
                color: #64748b;
                margin-bottom: 0.25rem;
            }
            .detail-text {
                font-size: 0.88rem;
                color: #cbd5e1;
                line-height: 1.45;
            }
            .impact-banner {
                background: linear-gradient(90deg, rgba(59,130,246,0.10), rgba(139,92,246,0.08));
                border: 1px solid rgba(99,102,241,0.25);
                border-radius: 10px;
                padding: 0.5rem 0.75rem;
                margin-top: 0.5rem;
                font-size: 0.85rem;
                color: #a5b4fc;
            }
            .impact-banner strong { color: #c7d2fe; }
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
