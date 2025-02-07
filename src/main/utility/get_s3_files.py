import boto3

from resources.dev.config import bucket_name, access0_key, Secret_access_key
from src.main.utility.encrypt_dycrypt_aws_key import decrypt
from src.main.utility.s3_client_obj import s3_bucket_access
from src.main.utility.sparksession import spark_session


def get_s3_files(bucket, prefix):
    """Fetch the list of files in an S3 bucket under a given prefix."""
    s3_client = s3_bucket_access(decrypt(access0_key),decrypt(Secret_access_key)).get_client()

    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    return [obj["Key"] for obj in response.get("Contents", [])] if "Contents" in response else []

# spark=spark_session()
# print(get_s3_files(bucket_name,"sales_data/"))