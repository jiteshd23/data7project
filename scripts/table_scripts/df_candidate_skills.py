import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle
from data7project.scripts.clean_scripts.clean_functions import *


def make_c_skills(bucket):  # breaks down dataframe into only relevant information.
    test = PullSingle(bucket)
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket=bucket)
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if 'Interview Notes' in key['Key']:
            dict_list.append(test.pull('Interview Notes', key['Key'][len('Interview Notes') + 1:]))
    for values in dict_list:
        for value in values['technologies']:
            outputs.append([values['name'], values["date"], value['language'], value['self_score']])
    skills = pd.DataFrame(outputs)
    skills.columns = ['name', "date", 'language', 'self score']
    skills = fix_date(skills, "date")
    skills = clean_name(skills, "name")
    # create a UNID based on name and date
    skills["UNID"] = skills["name"] + skills["date"]
    # drop name and date
    skills = skills.drop(['name', 'date'], axis=1)
    skills = skills[[skills.columns[2], skills.columns[0], skills.columns[1]]]
    return skills


