from config import Config
from os import path
import boto3, re

def run(key):
    s3 = boto3.resource('s3')
    file_name = re.sub(r'^[^/]+/', '', key)
    file = path.join(Config.PATHS['source'], file_name)
    s3.Bucket(Config.BUCKET_NAME).download_file(key, file)

    return file_name if path.isfile(file) else False
