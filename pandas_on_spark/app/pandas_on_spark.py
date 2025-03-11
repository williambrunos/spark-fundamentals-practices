import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("pandas_on_spark_app") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

print(spark)

spark.stop()