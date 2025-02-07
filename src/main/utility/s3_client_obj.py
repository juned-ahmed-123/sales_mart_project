import boto3

class s3_bucket_access:
    def __init__(self,aws_access_key,aws_Secret_key):
        self.aws_access_key=aws_access_key
        self.aws_Secret_key=aws_Secret_key
        self.session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_Secret_key
        )
        self.s3_client=self.session.client("s3")
    def get_client(self):
        return self.s3_client