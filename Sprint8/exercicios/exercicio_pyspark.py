from pyspark.sql import SparkSession, functions as f
from pyspark import SparkContext, SQLContext


# Etapa 1
spark = SparkSession.builder.master("local[*]").appName("Exercício Intro").getOrCreate()

caminho_csv = "nomes_aleatorios.txt"

df_nomes = spark.read.csv(caminho_csv)

df_nomes.show(5)

# Etapa 2
# df_nomes.printSchema()

df_nomes = df_nomes.withColumnRenamed('_c0', "Nomes")

# df_nomes.printSchema()
# df_nomes.show(10)

# Etapa 3

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    f.when(f.rand(seed=100) < 1/3, "Fundamental")
    .when(f.rand(seed=100) < 2/3, "Medio")
    .otherwise("Superior")
    )

# df_nomes.show(10)

# Etapa 4

lista_paises = ["Argentina", "Bolívia", "Brasil", "Chile",
                "Colômbia", "Equador", "Guiana", "Paraguai",
                "Peru", "Suriname", "Uruguai", "Venezuela",
                "Guiana Francesa"
                ]

df_nomes = df_nomes.withColumn(
    "Pais",
    f.when(f.rand(seed=100) < 1/13, lista_paises[0])
    .when(f.rand(seed=100) < 2/13, lista_paises[1])
    .when(f.rand(seed=100) < 3/13, lista_paises[2])
    .when(f.rand(seed=100) < 4/13, lista_paises[3])
    .when(f.rand(seed=100) < 5/13, lista_paises[4])
    .when(f.rand(seed=100) < 6/13, lista_paises[5])
    .when(f.rand(seed=100) < 7/13, lista_paises[6])
    .when(f.rand(seed=100) < 8/13, lista_paises[7])
    .when(f.rand(seed=100) < 9/13, lista_paises[8])
    .when(f.rand(seed=100) < 10/13, lista_paises[9])
    .when(f.rand(seed=100) < 11/13, lista_paises[10])
    .when(f.rand(seed=100) < 12/13, lista_paises[11])
    .otherwise(lista_paises[12])
    )

# df_nomes.show(10)

# Etapa 5

df_nomes = df_nomes.withColumn(
    "AnoNascimento",
    (f.rand(seed=42) * (2010 - 1945) + 1945).cast("int")
)

# df_nomes.printSchema()
# df_nomes.show(10)

# Etapa 6

df_select = df_nomes.select("*").filter(df_nomes.AnoNascimento > 2000)

# df_select.show(10)

# Etapa 7

df_nomes.createOrReplaceTempView("pessoas")

# spark.sql("select * from pessoas where AnoNascimento > 2000").show(10)

# Etapa 8

print(f"Existem {df_nomes.select('*')
      .filter((df_nomes.AnoNascimento > 1979) & (df_nomes.AnoNascimento < 1995))
      .count()} millenials no dataframe"
      )

# Etapa 9

spark.sql("""select count(*) as Millenials
        from pessoas
        where AnoNascimento > 1979 and AnoNascimento < 1995"""
          ).show()


# Etapa 10

df_geracao = spark.sql("""
                        select Pais,
                        case
                          when AnoNascimento > 1944 and AnoNascimento < 1965 then 'Baby Boomer'
                          when AnoNascimento >= 1965 and AnoNascimento < 1980 then 'Geracao X'
                          when AnoNascimento >= 1980 and AnoNascimento < 1995 then 'Millenials'
                          when AnoNascimento >= 1995 then 'Geracao Z'
                        end as Geracao,
                        count(*) as Quantidade
                        from pessoas
                        group by Pais, Geracao
                        order by Pais, Geracao, Quantidade"""
                        )

df_geracao.show(n=52)
