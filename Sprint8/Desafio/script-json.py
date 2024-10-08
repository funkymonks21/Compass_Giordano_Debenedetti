import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Carrega o arquivo json para um Dataframe dinâmico
df_json = glueContext.create_dynamic_frame.from_options(
    "s3",
    {"paths": ["s3://data-lake-giordano/Raw/TMDB/JSON/2024/9/19/filmes-sci-fi-steven.json"]},
    "json"
)

# Transforma o dataframe dinâmico em dataframe
df_spark = df_json.toDF()

# Excluo as colunas que não serão utilizadas, também renomeio algumas colunas para o mesmo nome das colunas do arquivo csv. No final eu excluo as linhas que estão com valores nulos
df_final = (df_spark.drop("genres", "release_date", "id", "name")
            .withColumnRenamed("imdb_id", "id")
            .withColumnRenamed("title", "tituloPrincipal")
            .na.drop())

# Transformo novamente para dataframe dinâmico.
df_dynamic = DynamicFrame.fromDF(df_final, glueContext, "dynamic_frame")

# Salvo o dataframe em um arquivo .parquet
glueContext.write_dynamic_frame.from_options(
    frame=df_dynamic,
    connection_type="s3",
    connection_options={"path": "s3://data-lake-giordano/Trusted/TMDB/2024/9/19/"},
    format="parquet"
)

job.commit()