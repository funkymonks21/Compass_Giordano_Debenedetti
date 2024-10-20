import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, floor
from pyspark.sql import Window
from pyspark.sql.functions import row_number
from datetime import datetime
from pyspark.sql.types import IntegerType


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Carrega os dados que foram tratados na sprint passada para um dataframe dinâmico
dyf_parquet = glueContext.create_dynamic_frame.from_options(
                connection_type="s3",
                format="parquet",
                connection_options={
                    "path": "s3://data-lake-giordano/Trusted/2024/9/19/stevenscifi.snappy.parquet",
                }
)

# Aqui eu realizo alguns testes para verificar se os dados foram passados corretamente
df = dyf_parquet.toDF()
df.show(9)
df.printSchema()

# Crio a dimesão tempo, usando o anoLancamento como base para determinar a década e o século do ano.
# Para determinar a década do ano, eu divido por 10 e multiplico por 10, essa operação trunca os dois últimos dígitos do ano. Ex: 2011 / 10 = 201 * 10 = 2010 <- Década de 2010
# Para o século a operação é parecida. Ex: 2011 / 100 = 20 + 1 = 21 <- Século 21
df_dim_tempo = df.select(
    col("anoLancamento"),
    (floor(col("anoLancamento") / 10) * 10).cast(IntegerType()).alias("decada"),
    (floor(col("anoLancamento") / 100) + 1).cast(IntegerType()).alias("seculo")
).distinct()

# Testes para verificar a integridade dos dados
df_dim_tempo.show()
df_dim_tempo.printSchema()

# Dimensão com os nomes dos filmes é criada aqui. Faço testes também para verificar a integridade dos dados.
df_dim_nome_filme = df.select("id", "titulo").distinct()
df_dim_nome_filme.show()
df_dim_nome_filme.printSchema()

# Aqui eu crio a dimensão dos gêneros, decidi usar os dados multivalorados.
# Precisei criar os ids dos gêneros, para isso, utilizei a função "window". Essa função cria um janela que contem os dados de "genero" ordenados e únicos.
# A segunda parte do bloco cria as "ids" usando o "row_number" e passando como parâmetro a "window_spec" que foi criada anteriormente com os nomes dos gêneros.
window_spec = Window.orderBy("genero")
df_dim_genero = df.select("genero").distinct() \
    .withColumn("idGenero", row_number().over(window_spec) - 1)
df_dim_genero.show()
df_dim_genero.printSchema()

# Por último, eu crio a tabela do Fato Filme.
# Dou um join entre o dataframe principal e o dataframe com a Dimensão de Gêneros. Faço testes no final para verificar a integridade e tipos dos dados
df_fato_filme = df.join(df_dim_genero, "genero", "left") \
    .select(
        "id",
        "idGenero",
        "anoLancamento",
        "tempoMinutos",
        "notaMediaIMDB",
        "numeroVotosIMDB",
        "notaMediaTMDB",
        "numeroVotosTMDB",
        "orcamento",
        "faturamento",
        "popularidadeTMDB"
    )
df_fato_filme.show()
df_fato_filme.printSchema()

# Aqui eu utilizo a função datetime para extrair a data local. Crio variáveis como ano, mês e dia para usar na criação do diretório onde serão salvos os ".parquet" com as tabelas 
current_date = datetime.now()
ano = current_date.year
mes = current_date.month
dia = current_date.day
path_base = f"s3://data-lake-giordano/Refined/{ano}/{mes}/{dia}/"

# Utilizo o coalesce para salvar os dataframes em um único arquivo
df_dim_tempo = df_dim_tempo.coalesce(1)
df_dim_nome_filme = df_dim_nome_filme.coalesce(1)
df_dim_genero = df_dim_genero.coalesce(1)
df_fato_filme = df_fato_filme.coalesce(1)

# Transformo todos os dataframes para dynamic frames, que serão utilizados para persistir os dados no Bucket do S3.
dyf_dim_tempo = DynamicFrame.fromDF(df_dim_tempo, glueContext, "dyf_dim_tempo")
dyf_dim_nome_filme = DynamicFrame.fromDF(df_dim_nome_filme, glueContext, "dyf_dim_nome_filme")
dyf_dim_genero = DynamicFrame.fromDF(df_dim_genero, glueContext, "dyf_dim_genero")
dyf_fato_filme = DynamicFrame.fromDF(df_fato_filme, glueContext, "dyf_fato_filme")

# Salvo os Dynamic Frames nos diretórios específicos para cada Tabela.
glueContext.write_dynamic_frame.from_options(
    frame=dyf_dim_tempo,
    connection_type="s3",
    format="parquet",
    connection_options={"path": path_base + "DimTempo"}
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_dim_nome_filme,
    connection_type="s3",
    format="parquet",
    connection_options={"path": path_base + "DimNomeFilme"}
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_dim_genero,
    connection_type="s3",
    format="parquet",
    connection_options={"path": path_base + "DimGenero"}
)

glueContext.write_dynamic_frame.from_options(
    frame=dyf_fato_filme,
    connection_type="s3",
    format="parquet",
    connection_options={"path": path_base + "FatoFilme"}
)

job.commit()