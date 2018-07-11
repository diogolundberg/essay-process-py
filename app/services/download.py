from config import Config
from os import path
import boto3, botocore

def run(key):
    s3 = boto3.resource('s3')
    file = path.join(Config.PATHS['source'], key)
    s3.Bucket(Config.BUCKET_NAME).download_file(key, file)

    return file if path.isfile(file) else False
