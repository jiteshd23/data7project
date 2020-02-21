import boto3
import pprint as pp
import json
import numpy as np
import pandas as pd
from io import StringIO

# below we are using the s3 service to store the files for the project.
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# from all the folders in the server, data7-engineering-project has teh most relevance to us.
contents = s3_client.list_objects(Bucket='data7-engineering-project')

# Below I have used a for loop to iterate through every file in the s3 bucket.
# for key in contents['Contents']:
#     print(key['Key'])

# We are looking at one file in the bucket.
s3object = s3_client.get_object(Bucket='data7-engineering-project',
                                Key='Academy/Business_36_2019-09-23.csv')
# pp.pprint(s3object)

# this will read the body of the file as that holds the information.
strbody = s3object['Body'].read()

pp.pprint(strbody)

contents = s3_client.list_objects(Bucket='data7-engineering-project')

# here a dataframe is made from the s3object

    str_body = strbody.decode('utf-8')
    StringData = StringIO(str_body)
    df = pd.read_csv(StringData, sep=',')

# print(df.describe())
print(df.loc[2])  # view of a row
df.fillna(value=0, inplace=True)  # fill the nan values with a 0 so its usable.
print(df.head())


# clean the values, all the columns other than names will be numeric
# change the nan values to 0 in order to keep the data types standardised.
# If the row contains any 0 values > 6 then add true to the failed column.
# if the last values of the csv dont have 0 then keep
# delete all the rows which are duplicates.

# here we make a column which shows the students who completed the course if they have a 0 present in their score.

def completedColumn():
    fail = []
    for i in df[df.columns[-1]]:
        if i < 1:
            fail.append(0)
        else:
            fail.append(1)
    df['Completed'] = fail
    # this creates column for the completed course.


completedColumn()
print(df)

# this is used to change the datatype in the df to int so its standardised.
score = df.columns[2:-1]
for i in score:
    df[i] = df[i].astype('int64')

# df[df.columns[2:]]
df.head()



