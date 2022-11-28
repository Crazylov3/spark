"""SimpleApp.py"""
from pyspark.sql import SparkSession

data_file = "data/airports.dat"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
airports = spark.read.csv(data_file, header=None, inferSchema=True)
airports.createOrReplaceTempView("airports")
# count the number of airports
spark.sql("SELECT COUNT(*) FROM airports").show()
spark.stop()
