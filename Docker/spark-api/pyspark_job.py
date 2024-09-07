from pyspark.sql import SparkSession

# Initialize Spark Session
def read_csv_from_hdfs(file_path):
    spark = SparkSession.builder \
        .appName("ReadCSVFromHDFS") \
        .config("spark.hadoop.fs.defaultFS", "hdfs://hadoop-master:9000") \
        .getOrCreate()

    # Read the CSV file from HDFS
    df = spark.read.csv(file_path, header=True)

    # Convert Spark DataFrame to Pandas DataFrame
    pandas_df = df.toPandas()

    # Return the result as JSON
    return pandas_df.to_json(orient="records")