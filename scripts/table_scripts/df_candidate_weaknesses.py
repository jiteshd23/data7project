import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle
from data7project.scripts.clean_scripts.clean_functions import *


# pulls file from aws when given the bucket name and outputs a dict


def make_c_weakness(bucket):  # breaks down dataframe into only relevant information.
    folder = 'Interview Notes'
    test = PullSingle(bucket)
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket=bucket)
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if folder in key['Key']:
            dict_list.append(test.pull(folder, key['Key'][len(folder) + 1:]))
    for values in dict_list:
        for value in values['weaknesses']:
            outputs.append([values['name'], values["date"], value])
    weaknesses = pd.DataFrame(outputs)
    weaknesses.columns = ['name', "date", 'weakness']
    weaknesses = fix_date(weaknesses, "date")
    weaknesses = clean_name(weaknesses, "name")
    # create a UNID based on name and date
    weaknesses["UNID"] = weaknesses["name"] + weaknesses["date"]
    weaknesses = weaknesses.drop(['name', 'date'], axis=1)
    return weaknesses
