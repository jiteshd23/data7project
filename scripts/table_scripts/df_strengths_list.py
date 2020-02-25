import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle

# pulls file from aws when given the bucket name and outputs a dict





def make_strength_list(folder):  # breaks down dataframe into only relevant information.
    test = PullSingle('data7-engineering-project')
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket='data7-engineering-project')
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if folder in key['Key']:
            dict_list.append(test.pull(folder,key['Key'][len(folder)+1:]))
    for values in dict_list:
        for value in values['strengths']:
            if value not in outputs:
                outputs.append(value)
    strength_list = pd.DataFrame(outputs)
    strength_list.columns = ['strengths']
    return strength_list

print(make_strength_list("Interview Notes"))


