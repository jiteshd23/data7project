import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle


def make_c_skills(bucket):  # breaks down dataframe into only relevant information.
    test = PullSingle(bucket)
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket=bucket)
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if 'Interview Notes' in key['Key']:
            dict_list.append(test.pull('Interview Notes',key['Key'][len('Interview Notes')+1:]))
    for values in dict_list:
        for value in values['technologies']:
            outputs.append([values['name'],value['language'],value['self_score']])
    skills = pd.DataFrame(outputs)
    skills.columns = ['name', 'language', 'self score']
    return skills

make_c_skills('data7-engineering-project')