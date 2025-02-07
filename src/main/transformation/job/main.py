from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType

from resources.dev.config import access0_key, Secret_access_key, mysql_url, mysql_properties, sales_data, \
    s3_source_directory, bucket_name
from src.main.utility.encrypt_dycrypt_aws_key import decrypt
from src.main.utility.get_processed_files import get_processed_files
from src.main.utility.get_s3_files import get_s3_files
from src.main.utility.process_new_files import process_new_files
from src.main.utility.s3_client_obj import s3_bucket_access
from src.main.utility.sparksession import spark_session
from src.main.utility.upload_localfiles_to_s3 import upload_files_to_s3

s3_client_provider=s3_bucket_access(decrypt(access0_key),decrypt(Secret_access_key))
s3_client=s3_client_provider.get_client()
resp=s3_client.list_buckets()
print(resp)
for bucket in resp["Buckets"]:
    print(bucket["Name"])
resp = s3_client.list_objects_v2(Bucket="sales-mart-project")

if "Contents" in resp:
    for obj in resp["Contents"]:
        print(obj["Key"])
else:
    print("No files found in the bucket.")
resp = s3_client.list_objects_v2(Bucket="sales-mart-project", Prefix="sales_data/")

if "Contents" in resp:
    for obj in resp["Contents"]:
        print("hai",obj["Key"])
else:
    print("No files found in sales_data/")

spark=spark_session()

# # df2 = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("s3a://sales-mart-project/sales_data/")
# # df2.show(10)
#
#
# df = spark.read.jdbc(url=mysql_url, table="product_staging_table", properties=mysql_properties)
# df.show()
# # customer_id,store_id,product_name,sales_date,sales_person_id,price,quantity,total_cost
schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("store_id", IntegerType(), True),
    StructField("product_name", StringType(), True),
    StructField("sales_date", DateType(), True),
    StructField("sales_person_id", IntegerType(), True),
    StructField("price",IntegerType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("total_cost", IntegerType(), True),
    # Add more columns as needed
])
df2 = spark.read \
    .format("csv") \
    .option("header", "true") \
    .schema(schema) \
    .load("s3a://sales-mart-project/sales_data/sales_data.csv")

df2.show()
# .csv(f"s3a://{bucket_name}/{s3_source_directory}")
# print(f"s3a://{s3_bucket}/{file}")
processed_files = get_processed_files(spark, mysql_url, mysql_properties)
print("processed_files",processed_files)
all_files = get_s3_files(bucket_name, s3_source_directory)
print("all_files",all_files)

new_files = list(set(all_files) - set(processed_files))
print("new_files",new_files)
process_new_files(spark, new_files, bucket_name, mysql_url, mysql_properties)