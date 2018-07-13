from config import Config
from os import path
import boto3

def run(key, file_name):
    s3 = boto3.resource('s3')
    file = path.join(Config.PATHS['source'], file_name)
    s3.Bucket(Config.BUCKET_NAME).download_file(key, file)

    return file if path.isfile(file) else False
