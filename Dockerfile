# Escolhendo uma imagem base enxuta e específica
FROM python:3.12.11-trixie

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência primeiro
COPY requirements.txt .

RUN pip install --upgrade pip

# Instala as dependências Python
RUN pip install -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta usada pela aplicação
EXPOSE 5000

# Comando padrão para iniciar a aplicação

CMD ["streamlit", "run", "Inicio.py", "--server.port=5000", "--server.address=0.0.0.0"]
