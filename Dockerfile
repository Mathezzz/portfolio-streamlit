# Escolhendo uma imagem base enxuta e específica
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência primeiro
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta usada pela aplicação
# EXPOSE 5000

# Comando padrão para iniciar a aplicação
CMD ["python", "Inicio.py"]
