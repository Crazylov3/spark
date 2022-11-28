import pyspark
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("Vu dep trai").getOrCreate()

airportsSchema = StructType() \
    .add("id", "integer") \
    .add("airport_name", "string") \
    .add("city", "string") \
    .add("country", "string") \
    .add("iata", "string") \
    .add("icao", "string") \
    .add("latitude", "float") \
    .add("longitude", "float") \
    .add("altitude", "integer") \
    .add("timezone", "byte") \
    .add("dst", "string") \
    .add("tz_database_timezone", "string") \
    .add("type", "string") \
    .add("source", "string")

routesSchema = StructType() \
    .add("airline", "string") \
    .add("airline_id", "integer") \
    .add("source_airport", "string") \
    .add("source_airport_id", "integer") \
    .add("destination_airport", "string") \
    .add("destination_airport_id", "integer") \
    .add("codeshare", "string") \
    .add("stops", "integer") \
    .add("equipment", "string")

airports = spark.read.csv("data/airports.dat", schema=airportsSchema)
airports.createOrReplaceTempView("airports")
airports.show(10)

routes = spark.read.csv("data/routes.dat", schema=routesSchema)
routes.show(10)
routes.createOrReplaceTempView("routes")

print("Number of airports: ")
spark.sql("SELECT COUNT(*) FROM airports").show()
print("_____________________________________________________________")
print("Number of airports DISTINCT: ")
spark.sql("SELECT COUNT(DISTINCT airport_name) FROM airports").show()
print("_____________________________________________________________")
print("Filtering airports in Greenland")
spark.sql("SELECT * FROM airports WHERE country = 'Greenland'").show()
print("_____________________________________________________________")
print("Grouping by country and counting")
spark.sql("SELECT country, COUNT(airport_name) AS airport_count FROM airports GROUP BY country").show(truncate=False)
print("_____________________________________________________________")
print("Joining routes and airports")
spark.sql("SELECT * FROM routes JOIN airports ON routes.source_airport_id = airports.id").show()
print("_____________________________________________________________")
print("Count the number of flights arriving in each country")
spark.sql(
    "SELECT country, COUNT(airport_name) AS airport_count "
    "FROM airports JOIN routes ON airports.id = routes.source_airport_id "
    "GROUP BY country"
).show(truncate=False)
