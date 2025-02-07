from pyspark.sql import SparkSession

from resources.dev.config import access0_key, Secret_access_key
from src.main.utility.encrypt_dycrypt_aws_key import decrypt


# spark=SparkSession.builder.appName().getOrCreate()
def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("mysqlconnector_spark2") \
        .config("spark.jars", ",".join([
        r"C:\BigData\hadoop-3.3.0\jar\mysql-connector-j-9.2.0.jar",
        r"C:\BigData\hadoop-3.3.0\jar\spark-hadoop-cloud_2.12-3.5.1.jar",
        r"C:\BigData\hadoop-3.3.0\jar\guava-27.0-jre.jar",
        r"C:\BigData\hadoop-3.3.0\jar\hadoop-aws-3.3.0.jar",
        r"C:\BigData\hadoop-3.3.0\jar\hadoop-common-3.3.0.jar",
        r"C:\BigData\hadoop-3.3.0\jar\aws-java-sdk-bundle-1.11.1026.jar"
    ])) \
        .config("spark.hadoop.fs.s3a.access.key", decrypt(access0_key)) \
        .config("spark.hadoop.fs.s3a.secret.key", decrypt(Secret_access_key)) \
        .config("spark.hadoop.fs.s3a.endpoint", "s3.ap-south-1.amazonaws.com") \
        .config("spark.hadoop.fs.s3a.connection.maximum", "100") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    return spark
# def spark_session():
#     spark = SparkSession.builder.master("local[*]") \
#         .appName("mysqlconnector_spark2")\
#         .config("spark.driver.extraClassPath", "C:\BigData\hadoop-3.3.0\jar\mysql-connector-j-9.2.0.jar;C:\BigData\hadoop-3.3.0\jar\hadoop-aws-3.3.0-javadoc;C:\BigData\hadoop-3.3.0\jar\aws-java-sdk-1.11.900") \
#         .config("spark.hadoop.fs.s3a.access.key", f"{decrypt(access0_key)}") \
#         .config("spark.hadoop.fs.s3a.secret.key", f"{decrypt(Secret_access_key)}") \
#         .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
#         .config("spark.hadoop.fs.s3a.connection.maximum", "100") \
#         .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
#         .getOrCreate()
#     # logger.info("spark session %s",spark)
#     return spark
# C:\BigData\hadoop-3.3.0\jar\hadoop-aws-3.3.0-javadoc