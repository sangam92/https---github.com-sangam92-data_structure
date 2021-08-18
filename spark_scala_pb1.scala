import org.apache.spark.sql.SparkSession

val spark = SparkSession
  .builder()
  .appName("Spark Scala Test")
  .getOrCreate()


val df = spark.read.format("text").option("header","true").load("test.txt")

df.show(5)

