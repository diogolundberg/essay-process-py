from config import Config
from os import path
import boto3

def run(key):
    aligned = open(path.join(Config.PATHS['aligned'], key), 'rb')
    cropped = open(path.join(Config.PATHS['cropped'], key), 'rb')

    s3 = boto3.resource('s3')
    s3.Bucket(Config.BUCKET_NAME).put_object(Key=f'aligned/{key}', Body=aligned)
    s3.Bucket(Config.BUCKET_NAME).put_object(Key=f'cropped/{key}', Body=cropped)

    return True
