import boto3
import json
import pandas as pd

# pulls file from aws when given the bucket name and outputs a dict

class PullJson2():

    def __init__(self, bucket):
        self._s3_client = boto3.client("s3")
        self._bucket = bucket


    def pull(self, file):
        file = self._s3_client.get_object(Bucket=self._bucket, Key= file)
        json_file = json.loads(file['Body'].read())
        return json_file



    def full_list(self):

        contents = self._s3_client.list_objects(Bucket=self._bucket)
        dict_list = []
        for key in contents['Contents']:
            if key['Key'][len(key['Key'])-1] == 'n':
                dict_list.append(self.pull(key['Key']))
        return dict_list

test = PullJson2('data7-engineering-project')
notes = test.full_list()
jsondf = pd.DataFrame(notes)
strengths = []
for values in jsondf['name']:
    strengths.append(jsondf['name'==values]['strengths'])
print(strengths)

