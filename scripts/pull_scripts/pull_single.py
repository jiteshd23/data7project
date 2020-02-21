# Importing our classes to use the methods
from data7project.scripts.pull_scripts.pull_json import PullJson
from data7project.scripts.pull_scripts.pull_txt import PullTxt
from data7project.scripts.pull_scripts.pull_csv import PullCsv

import boto3


# initing our client, and our classes into the Super class
class PullSingle:
    def __init__(self, bucket):
        self._bucket = bucket

    # sorting the files, by seeing if " " is in string
    def pull(self, folder, file, include_title=0):

        if ".json" in file:
            return PullJson(self._bucket).pull(folder, file)

        elif ".csv" in file:
            return PullCsv(self._bucket).pull(folder, file, include_title)

        elif ".txt" in file:
            return PullTxt(self._bucket).pull(folder, file)
