FROM python:3.12

WORKDIR /app

# Comando para instalar o boto3 no container
RUN pip install boto3 

# Copia o script e os arquivos csv para o container
COPY script.py /app/script.py
COPY movies.csv /app/movies.csv
COPY series.csv /app/series.csv

# Cria o volume para os dados não serem apagados
VOLUME [ "/data" ]

CMD [ "python", "/app/script.py" ]
