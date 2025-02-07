# aws credentials
# Access0_key="AKIA3RYC5VIJLPPPEU53"
from distutils.command.upload import upload

access0_key=b'Df2hDzMtC82j6/7yFeYB9XQ6MnSGldo5CCTMLfkvpCM='
# Secret_access_key="5gMWzydW2/krtPLuDuqpz81/m8MCPVdZamyNGHKX"
Secret_access_key=b'pY/kwrxtSvzL7a1m4XVbzosS4HIi0FPWDbNIApWdOKACh3pBy5GISMXBcUpH0DWn'
# encrypt_keys=encrypt("5gMWzydW2/krtPLuDuqpz81/m8MCPVdZamyNGHKX")
# print(encrypt_keys)
key="sales_mart_project"
iv="sales_mart_encrp"
salt="sales_mart_AesEncryption"
# aws bucket_name
bucket_name = "sales-mart-project"
# folder name in bucket name
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"

# local download location
local_directory = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\file_from_s3\\"
customer_data_mart_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\sales_partition_data\\"
error_folder_path_local = "C:\\Users\\nikita\\Documents\\data_engineering\\spark_data\\error_files\\"
# mysql config
mysql_properties = {
    "user": "root",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}
mysql_url = "jdbc:mysql://localhost:3306/sales_mart"

# local_directory to upload data in s3 buckets
sales_data="C:\csv_data\generated_csv_data\sales_data.csv"