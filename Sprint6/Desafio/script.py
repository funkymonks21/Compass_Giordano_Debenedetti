import boto3
from botocore.exceptions import ClientError  # Lib utilizada para retornar os possíveis erros na hora de criar o bucket ou carregar os arquivos.
import os  # Lib utilizada para extrair o nome dos arquivos csv da string do caminho dado.
from datetime import datetime  # Lib utilizada para extrair a data local do sistema.


def criar_bucket(s3_client, nome_bucket):
    # Esse método verifica se o bucket já foi criado, caso não tenha sido criado, ele cria. Caso dê algum erro, ele acusa qual foi o erro.
    try:
        # Verifica se o bucket já existe.
        s3_client.head_bucket(Bucket=nome_bucket)
        print(f'Bucket "{nome_bucket}" já existe.')
        return True
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            # Tenta criar o bucket, caso não consiga, ele retorna falso e indica qual foi o erro.
            try:
                s3_client.create_bucket(Bucket=nome_bucket)
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


def s3_key_gen(path_arquivo, s3_key_base):
    # Função para gerar o key com a formatação exigida pelo desafio
    # Utilizo a lib 'datetime' para extrar o dia do processamento.
    # A lib 'os' uso para extrair o nome do arquivo do caminho especificado.
    str_data = datetime.now().strftime("%Y/%m/%d")  # Extrai a data do sistema
    file_name = os.path.basename(path_arquivo)  # Extrai o nome do arquivo
    if 'movies' in file_name.lower():  # Gera o caminho de diretórios para o bucket
        s3_key_final = f'{s3_key_base}/Movies/{str_data}/{file_name}'
    elif 'series' in file_name.lower():
        s3_key_final = f'{s3_key_base}/Series/{str_data}/{file_name}'
    else:
        print('Nome do arquivo não reconhecido para Movies ou Series.')
        return None
    return s3_key_final


def upload_csv(s3_client, nome_bucket, path_arquivo, s3_key_base):
    # Função para carregar os arquivos Movies e Series para o bucket.
    s3_key_final = s3_key_gen(path_arquivo, s3_key_base)
    if s3_key_final:
        try:
            s3_client.upload_file(path_arquivo, nome_bucket, s3_key_final)
            print(f'Arquivo "{path_arquivo}" carregado com sucesso para o bucket "{nome_bucket}" com a chave "{s3_key_final}".')
        except ClientError as e:
            print(f'Erro ao subir o arquivo: {e}')


region = 'us-east-1'
s3_client = boto3.client('s3', region_name=region)
nome_bucket = 'data-lake-giordano'
path_arquivo_filmes = '/app/movies.csv'
path_arquivo_series = '/app/series.csv'
s3_key_base = 'Raw/Local/CSV'

if __name__ == '__main__':
    if criar_bucket(s3_client, nome_bucket):
        # Upload dos arquivos de Filmes e Series
        upload_csv(s3_client, nome_bucket, path_arquivo_filmes, s3_key_base)
        upload_csv(s3_client, nome_bucket, path_arquivo_series, s3_key_base)
