import boto3
import pandas as pd

from data7project.pull_scripts.pull_txt import PullTxt

# create an instance of pull text class
buckets = PullTxt("data7-engineering-project")
# create an instance of an S3 resource
s3 = boto3.resource("s3")
# create an instance of the Bucket
my_bucket = s3.Bucket("data7-engineering-project")
# initialise a count
count = 0
# initialise an empty list
txt_files = []
# append the file names to the txt_files list
for object_summary in my_bucket.objects.filter(Prefix="SpartaDays/"):
    file_name = object_summary.key.split("/")[1] # splits on the / to give just file name
    txt_files.append(file_name)

# iterate through the list of files, pull each as a df and append to previous
for file in txt_files:
    if count == 0:
        df = buckets.pull("SpartaDays", file)  # run the .pull method to bring data into df format from .txt
        count +=1  # increment count to ensure the df is not changed at the start of every iteration
    else:
        df = df.append(buckets.pull("SpartaDays", file))  # append to existing df if not first iteration

