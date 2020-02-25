import boto3
import json
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle



def make_weakness_list(folder):  # breaks down dataframe into only relevant information.
    test = PullSingle('data7-engineering-project')
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket='data7-engineering-project')
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if folder in key['Key']:
            dict_list.append(test.pull(folder,key['Key'][len(folder)+1:]))
    for values in dict_list:
        for value in values['weaknesses']:
            if value not in outputs:
                outputs.append(value)
    weakness_list = pd.DataFrame(outputs)
    weakness_list.columns = ['weaknesses']
    return weakness_list