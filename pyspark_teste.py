from pyspark.sql import SparkSession, SQLContext

spark = SparkSession.builder.appName('TB_YOUTUBE').getOrCreate()

sqlcontex = SQLContext(spark)

df = sqlcontex.read.csv(r'C:\Users\giova\OneDrive\Área de Trabalho\Code\USvideos.csv', header=True, inferSchema=True)

spark.catalog.clearCache()
