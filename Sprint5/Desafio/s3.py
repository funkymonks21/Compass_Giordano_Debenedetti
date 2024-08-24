import boto3
from botocore.exceptions import ClientError  # Lib utilizada para obter mensagens de erro, caso tenha algum problema com a execução do código.
import os  # Estou usando essa lib para pode referenciar a pasta do usuário com '~'


def criar_bucket(s3_client, nome_bucket, region):
    # Função para criar um bucket no s3, caso ele não exista.
    # Primeiro o script verifica se o bucket já existe, caso não exista, tenta criar um com nome estabelecido. Caso não consiga, apresenta o erro.
    try:
        s3_client.head_bucket(Bucket=nome_bucket)
        print(f'Bucket "{nome_bucket} já existe.')
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            try:
                s3_client.create_bucket(Bucket=nome_bucket,
                                         CreateBucketConfiguration={'LocationConstraint': region},
                                         )
                print(f'Bucket "{nome_bucket}" criado.')
                return True
            except ClientError as e:
                error_code = e.response['Error']['Code']
                if error_code == 'BucketAlreadyExists':
                    print(f'O nome "{nome_bucket}" já está em uso globalmente. Tente outro nome.')
                else:
                    print(f'Erro ao criar o bucket: {e}')
                return False
        else:
            print(f'Erro ao verificar o bucket: {e}')
            return False


def upload_csv(s3_client, nome_bucket, path_arquivo, nome_arq_s3):
    """
    Método para subir o arquivo da minha máquina para o s3.
    nome_bucket = nome do bucket no s3
    path_arquivo = Caminho local do arquivo
    nome_arq_s3 = Nome do arquivo no s3
    """
    try:
        s3_client.upload_file(path_arquivo, nome_bucket, nome_arq_s3)
        print(f'Arquivo "{path_arquivo}" subido com sucesso para o bucket "{nome_bucket}".')
    except ClientError as e:
        print(f'Erro ao subir o arquivo: {e}')


def query_s3(query, s3_client, nome_bucket, nome_arq_s3):
    # Função para fazer a consulta, e printar o resultado no console.
    resultado_query = s3_client.select_object_content(
        Bucket=nome_bucket,
        Key=nome_arq_s3,
        Expression=query,
        ExpressionType='SQL',
        InputSerialization={
                            'CSV':
                            {'FileHeaderInfo': 'USE',
                             'FieldDelimiter': ';'
                            }
        },
        OutputSerialization={'CSV': {}}
    )

    colunas = ["QUANTIDADE_TOTAL_FILMES_BR", "SOMA_PUBLICO_TOTAL", "FILMES_ACIMA_1_MILHAO", "FILMES_ABAIXO_1_MILHAO"]

    for event in resultado_query['Payload']:
        if 'Records' in event:
            # Decodifica e imprime o conteúdo dos registros
            output = event['Records']['Payload'].decode('utf-8')
            linhas = output.splitlines()
            valores = linhas[0].split(',')
            for coluna, valor in zip(colunas, valores):
                print(f'{coluna} - {valor}')


region = 'us-east-1'
s3_client = boto3.client('s3', region_name=region)
nome_bucket = 'bucket-desafio-giordano-debenedetti'
path_arquivo = os.path.expanduser('~/lancamentos-tratados.csv')
nome_arq_s3 = 'Dados-Bilheterias-Por-Distribuidoras.csv'

query = """
SELECT
    COUNT(*) AS QUANTIDADE_TOTAL_FILMES_BR,
    SUM(CAST(PUBLICO_TOTAL AS INT)) AS SOMA_PUBLICO_TOTAL,
    COUNT(CASE
            WHEN CHAR_LENGTH(PUBLICO_TOTAL) > 6 THEN 1
            END) AS FILMES_ACIMA_1_MILHAO,
    COUNT(CASE
            WHEN CHAR_LENGTH(PUBLICO_TOTAL) <= 6 THEN 1
            END) AS FILMES_ABAIXO_1_MILHAO
    FROM S3Object
    WHERE
        TIPO_OBRA = 'FICÇÃO'
        AND PAIS_OBRA = 'BRASIL'
        AND TO_TIMESTAMP(DATA_LANCAMENTO_OBRA) > TO_TIMESTAMP('2010-10-08T')
"""


if __name__ == "__main__":
    if criar_bucket(s3_client, nome_bucket, region):
        upload_csv(s3_client, nome_bucket, path_arquivo, nome_arq_s3)
query_s3(query, s3_client, nome_bucket, nome_arq_s3)