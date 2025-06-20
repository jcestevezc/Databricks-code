# Databricks notebook source
# Databricks notebook with key PySpark commands for data processing and analysis

# COMMAND ----------

# 1. Setup and Initialization
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("DatabricksPySparkTutorial").getOrCreate()

# Check Spark version
print(spark.version)

# Configure session (example: set driver memory)
spark = SparkSession.builder.appName("DatabricksPySparkTutorial").config("spark.driver.memory", "4g").getOrCreate()

# COMMAND ----------

# 2. Loading and Writing Data
# Read a CSV file
df = spark.read.csv("dbfs:/FileStore/sample_data.csv", header=True, inferSchema=True)

# Read a Parquet file
df_parquet = spark.read.parquet("dbfs:/FileStore/sample_data.parquet")

# Write data to Parquet
df.write.mode("overwrite").parquet("dbfs:/FileStore/output_data")

# Read from a Databricks table
df_table = spark.table("default.sample_table")

# COMMAND ----------

# 3. DataFrame Manipulation
# Display first 10 rows
df.show(n=10)

# Show schema
df.printSchema()

# Select specific columns
df.select("column1", "column2").show()

# Filter data
df_filtered = df.filter(df.column1 > 100)
df_filtered.show()

# Group and aggregate
df.groupBy("column1").agg({"column2": "sum"}).show()

# Sort data
df.orderBy("column1", ascending=False).show()

# Join DataFrames
df_joined = df.join(df_table, df.id == df_table.id, "inner")
df_joined.show()

# Handle nulls
df_no_nulls = df.na.drop()
df_filled = df.na.fill(0)

# Create new column
from pyspark.sql.functions import col, lit
df = df.withColumn("new_column", col("column1") * 2)
df = df.withColumn("constant", lit(100))

# COMMAND ----------

# 4. SQL in PySpark
# Register DataFrame as temporary table
df.createOrReplaceTempView("temp_table")

# Run SQL query
result = spark.sql("SELECT column1, COUNT(*) FROM temp_table GROUP BY column1")
result.show()

# COMMAND ----------

# 5. Common PySpark Functions
from pyspark.sql.functions import col, when, count, avg, max, min, round, to_date, current_date, datediff

# Conditional column
df = df.withColumn("category", when(col("column1") > 100, "High").otherwise("Low"))

# Work with dates
df = df.withColumn("date", to_date(col("date_column"), "yyyy-MM-dd"))
df = df.withColumn("days_diff", datediff(current_date(), col("date")))

# User-Defined Function (UDF)
from pyspark.sql.types import StringType
def my_function(x):
    return str(x * 2)
udf_my_function = udf(my_function, StringType())
df = df.withColumn("result", udf_my_function(col("column1")))

# COMMAND ----------

# 6. Optimization and Resource Management
# Cache DataFrame
df.cache()

# Clear cache
df.unpersist()

# Repartition data
df = df.repartition(10)
df = df.coalesce(2)

# View execution plan
df.explain()

# COMMAND ----------

# 7. Databricks-Specific Commands
# List files in DBFS
dbutils.fs.ls("dbfs:/FileStore/")

# Create a widget for interactivity
dbutils.widgets.text("parameter", "default_value")
value = dbutils.widgets.get("parameter")
print(f"Widget value: {value}")

# Example of mounting storage (replace with your credentials)
# dbutils.fs.mount(
#     source="s3://bucket-name",
#     mount_point="/mnt/mount_name",
#     extra_configs={"aws_access_key_id": "key", "aws_secret_access_key": "secret"}
# )

# COMMAND ----------

# 8. Machine Learning with MLlib
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

# Prepare data for ML
assembler = VectorAssembler(inputCols=["column1", "column2"], outputCol="features")
df_ml = assembler.transform(df)

# Train linear regression model
lr = LinearRegression(featuresCol="features", labelCol="target")
model = lr.fit(df_ml)
predictions = model.transform(df_ml)
predictions.show()

# COMMAND ----------

# 9. Delta Lake Handling
# Write to Delta table
df.write.format("delta").saveAsTable("default.delta_table")

# Optimize Delta table
spark.sql("OPTIMIZE default.delta_table")

# COMMAND ----------

# 10. Best Practices
# Avoid collecting large data
# df.collect()  # Use only for small DataFrames
df.show(5)  # Preferred for large data

# Use efficient formats like Delta
df.write.format("delta").save("dbfs:/FileStore/delta_table")
