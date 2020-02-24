
import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_txt import PullTxt
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from io import StringIO

# create class to take in bucket name and output a pd df merging all txt files within SpartaDays
class Append_Txt:
    def __init__(self, bucket):
    # create an instance of pull text class
        self.data = PullTxt(bucket)
    # create an instance of an S3 resource
        self.s3 = boto3.resource("s3")
    # create an instance of the Bucket
        self.my_bucket = self.s3.Bucket(bucket)

    def append_txt(self):
        # initialise a count
        count = 0
        # initialise an empty list
        txt_files = []
        # append the file names to the txt_files list
        for object_summary in self.my_bucket.objects.filter(Prefix="SpartaDays/"):
            file_name = object_summary.key.split("/")[1] # splits on the / to give just file name
            txt_files.append(file_name)
# iterate through the list of files, pull each as a df and append to previous
        for file in txt_files:
            if count == 0:
                df = self.data.pull("SpartaDays", file)  # run the .pull method to bring data into df format from .txt
                count +=1  # increment count to ensure the df is not changed at the start of every iteration
            else:
                sparta_days = df.append(self.data.pull("SpartaDays", file))  # append to existing df if not first iteration
        return sparta_days

# class Append_Csv:
#     def __init__(self, bucket):
#     # create an instance of pull text class
#         self.data = PullCsv(bucket)
#     # create an instance of an S3 resource
#         self.s3 = boto3.resource("s3")
#     # create an instance of the Bucket
#         self.my_bucket = self.s3.Bucket(bucket)
#
#     def append_csv(self):
#         # initialise a count
#         count = 0
#         # initialise an empty list
#         txt_files = []
#         # append the file names to the txt_files list
#         for object_summary in self.my_bucket.objects.filter(Prefix="Talent/"):
#             file_name = object_summary.key.split("/")[1] # splits on the / to give just file name
#             txt_files.append(file_name)
# # iterate through the list of files, pull each as a df and append to previous
#         for file in txt_files:
#             if count == 0:
#                 df = self.data.pull("Talent", file)  # run the .pull method to bring data into df format from .txt
#                 count +=1  # increment count to ensure the df is not changed at the start of every iteration
#             else:
#                 sparta_days = df.append(self.data.pull("Talent", file))  # append to existing df if not first iteration
#         return sparta_days
#
# aa = Append_Csv("data7-engineering-project")
# print(aa.append_csv().head())