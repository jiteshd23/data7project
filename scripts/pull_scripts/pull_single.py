# Importing our classes to use the methods
from data7project.scripts.pull_scripts.pull_json import *
from data7project.scripts.pull_scripts.pull_txt import *
from data7project.scripts.pull_scripts.pull_csv import *

# importing to check filepath exists
import os.path
# importing json and pandas to read json files locally
import json
import pandas as pd

import boto3

print()

# initing our client, and our classes into the Super class
class PullSingle:
    def __init__(self, bucket):
        self._bucket = bucket

    # sorting the files, by seeing if " " is in string
    def pull(self, folder, file, include_title=0):
        dir_link = f'{os.path.abspath(__file__)[:-len("pull_single.py")]}/{folder}_{file})'.replace(' ', '-')
        if os.path.isfile(dir_link):
            if ".json" in file:
                with open(dir_link) as json_file:
                    return json.load(json_file)
            else:
                return pd.read_csv(dir_link)

        else:
            if ".json" in file:
                dict_value = PullJson(self._bucket).pull(folder, file)
                with open(dir_link, 'x') as json_file:
                    json.dump(dict_value, json_file)
                return dict_value

            elif ".csv" in file:
                pd_value = PullCsv(self._bucket).pull(folder, file, include_title)
                pd_value.to_csv(dir_link, mode='x')
                return pd_value

            elif ".txt" in file:
                pd_value = PullTxt(self._bucket).pull(folder, file)
                pd_value.to_csv(dir_link, mode='x')
                return pd_value

