import boto3
from io import StringIO
import pandas as pd


class PullCsv:
    def __init__(self, bucket):  # when creating class, input bucket name as variable
        self.s3_client = boto3.client('s3')  # making client
        s3_resource = boto3.resource('s3')
        self.bucket2 = bucket
        Contents = self.s3_client.list_objects(Bucket=bucket)  # selecting bucket

    def pull(self, folder, file):  # use method pull on instance class PullCsv, specifying folder and filename
        s3object = self.s3_client.get_object(Bucket=self.bucket2, Key=folder + '/' + file)  # selecting file and folder

        strbody = s3object['Body'].read()  # reads body of object

        str_body = strbody.decode('utf-8')  # decodes field
        StringData = StringIO(str_body)
        df = pd.read_csv(StringData, sep=',')  # turns into dataframe

        return df
