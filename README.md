# Portfólio em Streamlit

Aplicação de portfólio pessoal construída com Streamlit para apresentar perfil profissional, trajetória e projetos em dados, IA e automação.

## Visão Geral

O app está organizado no formato multipage do Streamlit:

- Página inicial com apresentação, links e currículo.
- Página de projetos com cards, links e sistema de avaliação via Google Sheets.
- Página "Sobre Mim" com storytelling da trajetória.

## Estrutura do Projeto

```text
Portfolio-streamlit/
├── Inicio.py
├── portfolio/
│   ├── __init__.py
│   ├── feedback.py
│   ├── project_data.py
│   └── ui_components.py
├── pages/
│   ├── 1_Projetos.py
│   └── 2_Sobre_Mim.py
├── assets/
├── static/
├── requirements.txt
├── Dockerfile
└── .gitignore
```

### O papel de cada parte

- `Inicio.py`
  - Define a home do portfólio.
  - Carrega foto, texto de apresentação, links e botão para download do currículo em `static/`.

- `pages/1_Projetos.py`
  - Exibe projetos em cards com filtros, busca e paginação.
  - Usa componentes do `streamlit-shadcn-ui` para navegação e ações.
  - Integra área de prova social por projeto (média, votos, gráfico e comentários).

- `portfolio/project_data.py`
  - Catálogo único dos projetos (dados estruturados para renderização).

- `portfolio/ui_components.py`
  - Componentes e tema visual reutilizável da UI.

- `portfolio/feedback.py`
  - Camada de avaliação com leitura/escrita no Google Sheets.
  - Padroniza colunas e trata fallback offline.

- `pages/2_Sobre_Mim.py`
  - Mostra trajetória profissional/acadêmica em formato narrativo.

- `assets/`
  - Imagens usadas nas páginas.

- `static/`
  - Arquivos estáticos para download (ex.: currículo PDF).

- `.env`
  - Variáveis de ambiente locais.
  - Principal variável esperada no projeto: `GCP_SERVICE_ACCOUNT` contendo o JSON da service account em formato string.

## Fluxo de Funcionamento

1. O Streamlit inicia por `Inicio.py`.
2. O diretório `pages/` é detectado automaticamente e vira o menu lateral de navegação.
3. Na página de projetos:
   - As credenciais são lidas via `.env`.
   - O app autentica no Google Sheets.
   - Avaliações são carregadas para exibição de gráfico e histórico.
   - Novas avaliações são enviadas para a planilha.

## Como Rodar Localmente

### Pré-requisitos

- Python 3.11+ (ideal: 3.12)
- `pip`

### Passos

1. Criar e ativar ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Criar arquivo `.env` na raiz com a credencial:

```env
GCP_SERVICE_ACCOUNT={"type":"service_account", ...}
```

4. Executar o app:

```bash
streamlit run Inicio.py
```

## Docker

Existe um `Dockerfile` para containerização do app. Antes de uso em produção, recomenda-se revisar comandos de build/run e validações do container.

## Melhorias Planejadas

As próximas evoluções de UI/UX e organização da página de projetos estão descritas em `planejamento.md`.