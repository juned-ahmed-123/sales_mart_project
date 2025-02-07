import os

import boto3

from resources.dev.config import access0_key, Secret_access_key
from src.main.utility.encrypt_dycrypt_aws_key import encrypt1, decrypt
from src.main.utility.s3_client_obj import s3_bucket_access
#
# def upload_files_to_s3(file_name,bucket_name,s3_key):
#     getclient_s3=s3_bucket_access(decrypt(access0_key),decrypt(Secret_access_key))
#     s3=getclient_s3.get_client()
#     s3.upload_file(file_name, bucket_name, s3_key)
#     # print(s3)
#     # print("s3_path",s3_path)

def upload_files_to_s3(file_name, bucket_name, s3_key):
    try:
        # Ensure the file exists locally before uploading
        if not os.path.exists(file_name):
            print(f"Error: The file {file_name} does not exist.")
            return

        # Create an instance of the s3_bucket_access class
        getclient_s3 = s3_bucket_access(decrypt(access0_key), decrypt(Secret_access_key))

        # Get the s3 client
        s3 = getclient_s3.get_client()

        # Upload the file to S3
        s3.upload_file(file_name, bucket_name, s3_key)
        print(f"File {file_name} uploaded successfully to s3://{bucket_name}/{s3_key}")

    except boto3.exceptions.S3UploadFailedError as e:
        print(f"Upload failed: {e}")
    except Exception as e:
        print(f"Error: {e}")