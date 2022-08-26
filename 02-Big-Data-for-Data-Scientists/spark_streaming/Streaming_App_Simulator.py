from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Define a nossa aplicação Spark
spark = SparkSession \
    .builder \
    .appName("StructuredStreamingStackApp") \
    .getOrCreate()

# nome do arquivo para definicao do schema
arquivo = "data/landing/2010-summary.json"

# diretório com os arquivos jsons
diretorio = "data/landing"

# ler o arquivo para definir schema
df = spark.read.json(arquivo)
schema_df = df.schema

# imprime o schema do dataframe
df.printSchema()

# lendo os arquivos e cria o dataframe em streaming
df_streaming = spark.readStream\
    .schema(schema_df)\
    .option("maxFilesPerTrigger", "1") \
    .json(diretorio)

# processa dados em streaming
resultado = df_streaming.groupBy("ORIGIN_COUNTRY_NAME").sum("count")

# escreve a saida do processamento para o console.
saida = resultado.writeStream\
    .outputMode("update")\
    .format("console") \
    .start()

# imprime o resultado até que a aplicação seja encerrada
saida.awaitTermination()