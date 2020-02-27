import boto3
import json
import pandas as pd
from data7project.scripts.pull_scripts.pull_single import PullSingle
from data7project.scripts.clean_scripts.clean_functions import *

# pulls file from aws when given the bucket name and outputs a dict




def make_interview(bucket):  # breaks down dataframe into only relevant information.
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
        outputs.append([values['name'],values['date'],values['course_interest'],values['geo_flex'],values['financial_support_self'],values['result']])
    interviews= pd.DataFrame(outputs)
    interviews.columns = ['name', 'date', 'course_interest', 'geo flex', 'financial self support', 'interview pass']
    interviews = fix_date(interviews, "date")
    interviews = clean_name(interviews, "name")
    # create a UNID based on name and date
    interviews["UNID"] = interviews["name"] + interviews["date"]
    interviews = interviews.drop(['name', 'date'], axis=1)
    return interviews



