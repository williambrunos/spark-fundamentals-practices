import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("pandas_on_spark_app") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

business_data = ps.read_json("data/business.json", lines=True)
reviews_data = ps.read_json("data/reviews.json", lines=True)
users_data = ps.read_json("data/users.json", lines=True)

print(f"\n\nusers data: \n\n{users_data.describe()}\n\n")

spark.stop()
