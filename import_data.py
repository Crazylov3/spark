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
airports.show(10)

routes = spark.read.csv("data/routes.dat", schema=routesSchema)
routes.show(10)

print("Number of airports: ", airports.count())
print("_____________________________________________________________")
print("Number of airports DISTINCT: ")
airports.select(countDistinct("airport_name")).show()
print("_____________________________________________________________")

print("Filtering airports in Greenland")
airports.filter(airports.country == "Greenland").show()
print("_____________________________________________________________")

print("Grouping by country and counting")
groupby_country_airports = (
    airports
    .groupBy("country")
    .agg(count("airport_name").alias("airport_count"))
    .show(truncate = False)
)
print("_____________________________________________________________")
print("Joining routes and airports")
routes_join_airports = routes.join(airports, routes.destination_airport_id == airports.id, "left")
routes_join_airports.show()

print("_____________________________________________________________")
print("Count the number of flights arriving in each country")
airport_counts = (
    routes_join_airports
    .groupBy("country")
    .agg(count("destination_airport").alias("flight_arriving_count"))
    .show(truncate = False)
)