import pandas as pd

# Script em python para modificar a formatação da coluna "RENDA_TOTAL" do CSV. Transformei para float.
# Também converti o tipo da coluna 'PUBLICO_TOTAL' para inteiro. Converti a coluna 'DATA_LANCAMENTO_OBRA' para fomato de data.
# Fiz esse script, pois o S3 Select não suporta a função REPLACE do SQL, que seria a minha opção para modificar os dados.
df = pd.read_csv('lancamentos-comerciais-por-distribuidoras.csv', delimiter=';')

df['RENDA_TOTAL'] = df['RENDA_TOTAL'].str.replace('R\$', '', regex=True)
df['RENDA_TOTAL'] = df['RENDA_TOTAL'].str.replace('.', '', regex=False)
df['RENDA_TOTAL'] = df['RENDA_TOTAL'].str.replace(',', '.', regex=False)
df['DATA_LANCAMENTO_OBRA'] = pd.to_datetime(df['DATA_LANCAMENTO_OBRA'], format='%d/%m/%Y')

# Agora eu vou desconsiderar filmes duplicados para a minha análise.
# Optei por desconsiderar filmes com o nome, tipo e pais iguais.
df = df.groupby(['TITULO_ORIGINAL', 'TIPO_OBRA', 'PAIS_OBRA']).agg(
    DATA_LANCAMENTO_OBRA=('DATA_LANCAMENTO_OBRA', 'first'),
    CPB_ROE=('CPB_ROE', 'first'),
    PUBLICO_TOTAL=('PUBLICO_TOTAL', 'sum'),
    RENDA_TOTAL=('RENDA_TOTAL', 'sum'),
    RAZAO_SOCIAL_DISTRIBUIDORA=('RAZAO_SOCIAL_DISTRIBUIDORA', 'first'),
    REGISTRO_DISTRIBUIDORA=('REGISTRO_DISTRIBUIDORA', 'first'),
    CNPJ_DISTRIBUIDORA=('CNPJ_DISTRIBUIDORA', 'first')
).reset_index()

# Código para ordenar as linhas pela data de lançamento, visto que o meu group by bagunçou tudo.
df = df.sort_values(by='DATA_LANCAMENTO_OBRA', ascending=False)
# Reordenar as colunas para que a coluna de data de lançamento seja a primeira
cols = ['DATA_LANCAMENTO_OBRA'] + [col for col in df.columns if col != 'DATA_LANCAMENTO_OBRA']
df = df[cols]
# Adiciona "T" no final da data, para poder usar com as funções de Date do S3
df['DATA_LANCAMENTO_OBRA'] = df['DATA_LANCAMENTO_OBRA'].dt.strftime('%Y-%m-%d') + 'T'

df.to_csv('lancamentos-tratados.csv', sep=';', index=False)