import boto3
import json

# pulls file from aws when given the bucket name and outputs a dict

class PullJson2():

    def __init__(self, bucket):
        self._s3_client = boto3.client("s3")
        self._s3_resource = boto3.resource("s3")
        self._bucket = bucket

        # reads the json file, ou
    def pull(self, file):
        file = self._s3_client.get_object(Bucket=self._bucket, Key= file)
        json_file = json.loads(file['Body'].read())
        return json_file



    def find(self,keyfactor):
        s3_client = boto3.client("s3")
        contents = s3_client.list_objects(Bucket='data7-engineering-project')
        strengths = []
        for key in contents['Contents']:
            if key['Key'][len(key['Key'])-1] == 'n':
                for x in test.pull(key['Key'])[keyfactor]:
                    if x not in strengths:
                        strengths.append(x)
        return strengths

test = PullJson2('data7-engineering-project')
test.find('strengths')
