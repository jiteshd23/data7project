import boto3
import json
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle







def make_c_skills(folder):  # breaks down dataframe into only relevant information.
    test = PullSingle('data7-engineering-project')
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket='data7-engineering-project')
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if folder in key['Key']:
            dict_list.append(test.pull(folder,key['Key'][len(folder)+1:]))
    for values in dict_list:
        for value in values['technologies']:
            outputs.append([values['name'],value['language'],value['self_score']])
    skills = pd.DataFrame(outputs)
    skills.columns = ['name', 'language', 'self score']
    return skills

