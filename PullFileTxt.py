import boto3
import pprint as pp
import json
import numpy as np
import pandas as pd



class PullFile_Txt():
    def __init__(self, bucket):
        self._s3_client = boto3.client("s3")
        self._s3_resource = boto3.resource("s3")
        self._bucket = bucket

    def get_txt(self):
