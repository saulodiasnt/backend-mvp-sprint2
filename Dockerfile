# Use a imagem oficial do Python como imagem base
FROM python:3.8-slim-buster

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências e instala as dependências
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do seu projeto para o diretório de trabalho
COPY . .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
