# Escolhendo uma imagem base enxuta e específica
FROM python:3.12.11-trixie

RUN apt-get update && apt-get install

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência primeiro
COPY requirements.txt .

# Instala as dependências Python
RUN pip install -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta usada pela aplicação
# EXPOSE 5000

# Comando padrão para iniciar a aplicação
CMD ["python", "Inicio.py"]
