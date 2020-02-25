import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle



def make_weakness_list(bucket):  # breaks down dataframe into only relevant information.
    folder = 'Interview Notes'
    test = PullSingle(bucket)
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket=bucket)
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
    # add a unique Id
    weakness_list.insert(0, 'weakness_id', range(1, 1 + len(weakness_list)))
    return weakness_list
