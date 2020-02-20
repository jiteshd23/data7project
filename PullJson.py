import boto3
import json

#pulls file from aws when given the bucket name and outputs a dict
class PullFileJson():

    def __init__(self, bucket):
        self._s3_client = boto3.client("s3")
        self._s3_resource = boto3.resource("s3")
        self._bucket = bucket

    #reads the json file, ou
    def pull(self, folder, file):
        file = self._s3_client.get_object(Bucket=self._bucket, Key=folder+"/"+file)
        json_file = json.loads(file['Body'].read())
        return json_file








