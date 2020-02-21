import boto3
from io import StringIO
import pandas as pd


# class to pull csv, pull returns a pd df object. can take optional title argument in pull to include title in
# a final column list
class PullCsv:
    def __init__(self, bucket):  # when creating class, input bucket name as variable
        self.s3_client = boto3.client('s3')  # making client
        self.bucket2 = bucket

        # use method pull on instance class PullCsv, specifying folder and filename

    def pull(self, folder, file, include_filename=0):
        s3object = self.s3_client.get_object(Bucket=self.bucket2, Key=folder + '/' + file)  # selecting file and folder

        strbody = s3object['Body'].read()  # reads body of object

        str_body = strbody.decode('utf-8')  # decodes field
        StringData = StringIO(str_body)
        df = pd.read_csv(StringData, sep=',')  # turns into dataframe object
        if include_filename == 1:
            df['title'] = file

        return df

