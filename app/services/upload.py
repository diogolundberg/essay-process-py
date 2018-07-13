from config import Config
from os import path
import boto3

def run(file_name):
    aligned = open(path.join(Config.PATHS['aligned'], file_name), 'rb')
    cropped = open(path.join(Config.PATHS['cropped'], file_name), 'rb')

    s3 = boto3.resource('s3')
    s3.Bucket(Config.BUCKET_NAME).put_object(Key=f'aligned/{file_name}', Body=aligned)
    s3.Bucket(Config.BUCKET_NAME).put_object(Key=f'cropped/{file_name}', Body=cropped)

    return True
