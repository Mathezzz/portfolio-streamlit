# Como adicionar um projeto ao portfólio

Edite **apenas** o arquivo `portfolio/project_data.py`.
Adicione um novo dicionário à lista `PROJECTS` seguindo a estrutura abaixo.

---

## Estrutura completa

```python
{
    "id": "slug-unico-do-projeto",          # string, sem espaços, sem acentos
    "nome": "Nome do Projeto",              # string, aparece como título do card
    "categoria": "Automação",              # categoria PRIMÁRIA (define cor do chip principal)
    "categorias": ["Automação", "IA"],     # lista de categorias — controla em quais abas o projeto aparece
    "ano": "2025",                          # string
    "status": "Em produção",               # "Publicado" | "Em produção" | "Protótipo" | "Em evolução"
    "resumo": "Frase curta de impacto.",    # ~1-2 linhas, aparece no card sem expandir
    "objetivo": "O que o projeto resolve.", # aparece no expander — coluna Objetivo
    "solucao": "Como foi feito.",          # aparece no expander — coluna Solução
    "resultado": "O que foi alcançado.",   # aparece no expander — coluna Resultado
    "impacto": "Linha de destaque.",       # opcional — aparece como banner abaixo do grid de detalhes
    "stack": ["Ferramenta1", "Ferramenta2"],  # lista de tecnologias usadas (badges)
    "imagem": "assets/nome-do-arquivo.png",  # caminho relativo à raiz do projeto
    "links": {
        "demo": "https://...",             # opcional — botão "Ver demo"
        "publicacao": "https://...",       # opcional — botão "Ver publicação" (usado se não houver demo)
        "github": "https://...",           # opcional — botão "Repositório"
    },
}
```

---

## Categorias disponíveis

| Valor        | Ícone | Cor do chip   | Quando usar                                  |
|--------------|-------|---------------|----------------------------------------------|
| `"IA"`       | 🤖    | Roxo          | Modelos, agentes, LLMs, visão computacional  |
| `"BI"`       | 📊    | Verde         | Dashboards, relatórios, Looker, Power BI     |
| `"Dados"`    | 🔢    | Azul          | Pipelines, ETL, análise exploratória, OCR    |
| `"Automação"`| ⚙️    | Âmbar         | N8N, scripts, IoT, RPA, integrações          |

Para que o projeto apareça em **mais de uma aba**, liste todas as categorias em `categorias`.  
O campo `categoria` define apenas a cor do chip primário no card.

---

## Imagem de capa

- Coloque o arquivo em `assets/`
- Formatos aceitos: `.png`, `.jpg`, `.jpeg`
- Resolução recomendada: **1200 × 700 px** (proporção 12:7)
- Se a imagem não existir, o card exibe um fundo escuro neutro sem quebrar o app

---

## Status disponíveis

| Valor           | Significado                              |
|-----------------|------------------------------------------|
| `"Publicado"`   | Disponível publicamente                  |
| `"Em produção"` | Rodando em ambiente real de uso          |
| `"Protótipo"`   | Funcional mas não em uso contínuo        |
| `"Em evolução"` | Em desenvolvimento ativo                 |

---

## Links

Todos os links são **opcionais**. Regras de exibição dos botões:

- Se `demo` existir → botão **"Ver demo"**
- Se não houver `demo` mas houver `publicacao` → botão **"Ver publicação"**
- Se `github` existir → botão **"Repositório"**
- Se `github` não existir → botão desabilitado **"Repositório em breve"**
- Se não houver nenhum link → nenhum botão é renderizado

---

## Exemplo mínimo

```python
{
    "id": "meu-projeto",
    "nome": "Meu Projeto",
    "categoria": "Dados",
    "categorias": ["Dados"],
    "ano": "2025",
    "status": "Protótipo",
    "resumo": "Uma linha explicando o que o projeto faz.",
    "objetivo": "Por que foi feito.",
    "solucao": "Como foi feito.",
    "resultado": "O que gerou.",
    "impacto": "",
    "stack": ["Python", "Pandas"],
    "imagem": "assets/meu-projeto.png",
    "links": {},
}
```
