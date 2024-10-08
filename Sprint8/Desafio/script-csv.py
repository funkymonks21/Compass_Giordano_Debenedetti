import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Carrega o arquivo movies.csv para um dataframe dinâmico
df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": ["s3://data-lake-giordano/Raw/Local/CSV/Movies/2024/09/07/movies.csv"]
        },
        "csv",
        {"withHeader": True, "separator": "|"},
        )

# Transforma o dataframe dinâmico em dataframe spark
df_spark = df.toDF()
# Substituo os valores "\N" para nulos
df_spark = df_spark.replace("\\N", None)

# Aqui eu estou querendo apenas os filmes de sci-fi. Exluo algumas colunas que não serão utilizadas para a análise.
# Excluo linhas com valores nulos nas colunas que utilizarei para minha análise.
# Excluo filmes duplicados, mantendo apenas a primeira aparição do filme
df_final = (df_spark.filter(df_spark["genero"].contains("Sci-Fi"))
               .na.drop(subset=["tempoMinutos", "notaMedia", "numeroVotos"])
               .drop("generoArtista", "personagem", "nomeArtista", 
                     "anoNascimento", "anoFalecimento", "profissao", 
                     "titulosMaisConhecidos")
                     .dropDuplicates(["id"]
            )
)

# Passo o dataframe para um único arquivo
df_final_coa = df_final.coalesce(1)

# Passo o dataframe spark para dataframe dinânimo
df_dynamic = DynamicFrame.fromDF(df_final_coa, glueContext, "dynamic_frame")

# Salvo o arquivo na camada Trusted
glueContext.write_dynamic_frame.from_options(
    frame=df_dynamic,
    connection_type="s3",  
    connection_options={"path": "s3://data-lake-giordano/Trusted/CSV/"},
    format="parquet" 
)

job.commit()