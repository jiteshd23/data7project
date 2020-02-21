#### NEEDS TO IMPORT THE BELOW PullTxt to function:
import boto3
import pandas as pd
from data7project.scripts.pull_scripts.pull_txt import PullTxt

######
# CODE TO GENERATE DATE AND LOC of Sparta Days & Name/Pyscho/Present scores for attendees
# create an instance of pull text class
data = PullTxt("data7-engineering-project")
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
        df = data.pull("SpartaDays", file)  # run the .pull method to bring data into df format from .txt
        count +=1  # increment count to ensure the df is not changed at the start of every iteration
    else:
        sparta_days = df.append(data.pull("SpartaDays", file))  # append to existing df if not first iteration

# return only the unique entries for both date & location
date_loc = (sparta_days.groupby(['Date','Location']).size().reset_index())
# drop the last column to display just date and location
date_loc = date_loc.drop(date_loc.columns[-1], axis=1)
# drop the Date & location columns to display just name, psycho and present scores
name_psy_pres = sparta_days.drop(["Date", "Location"], axis=1)

print(date_loc.head())
print(name_psy_pres.head())