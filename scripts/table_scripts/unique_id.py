## can be further productionised
# below generates a dataframe which will have a unique talent_id number to be maintained throughout the system
# name, interview_date & start course date - with this information all other tables can be merged to allow the unique ID to be used
# accurately throughout
#

from data7project.scripts.clean_scripts.clean_functions import *
from data7project.scripts.table_scripts.df_course_schedule import *
import pandas as pd

def unique_talent(bucket):
    # takes in talent csvs as one and appends
    talent = Append_All(bucket).append_all("Talent")
    # fills na for date
    talent["invited_date"] = talent["invited_date"].fillna(0)
    #converts to int
    talent["invited_date"] = talent["invited_date"].astype(int)
    # converts to string
    talent["invited_date"] = talent["invited_date"].astype(str)
    # concatenates the date
    talent["invite_date"] = talent["month"] + " " + talent["invited_date"]
    # drops the old date
    talent = talent.drop(['month', 'invited_date'], axis=1)
    # drops the old date
    talent = talent.drop(["id"], axis=1)
    # fixes date to workabale format
    talent = fix_date(talent, "invite_date")
    # drops duplicates based on name and and invited date
    talent = talent.drop_duplicates(subset=['name', 'invite_date'], keep='last')
    #returns only name and invite_date
    return talent[["name","invite_date"]]


def unique_course(bucket):
    academy = Append_All(bucket).append_all("Academy", include_title=1)
    # new data frame with split value columns on the underscore
    new = academy["title"].str.split("_", n=2, expand=True)
    # making separate course name column from new data frame
    academy["course"] = new[0]
    # making separate course name column from new data frame
    academy["course_number"] = new[1]
    # making separate start date column from new data frame
    academy["start_date"] = new[2]
    # Dropping old title columns
    academy.drop(columns=["title"], inplace=True)
    # remove .csv from the filename in the start_date column
    academy["start_date"] = academy["start_date"].str.replace('.csv', '')
    # returns an ordered list of unique courses from all csvs using course and course number
    academy = academy.sort_values(['course', "course_number"], ascending=True)
    # returns only name and start_date
    return academy[["name", "start_date"]]


talent = unique_talent("data7-engineering-project")
academy = unique_course("data7-engineering-project")
# converts the date string to date time for comparison in both dataframes
talent['invite_date'] = pd.to_datetime(talent['invite_date'])
academy['start_date'] = pd.to_datetime(academy['start_date'])

#### THERE IS A WAY TO DO THIS IN MUCH MORE "PYTHON" EFFICIENT WAY
# creates an empty list
list = []
# iterates through each row of the talent table and creates a list of lists of name and invite date
for index, row in talent.iterrows():
    l = []
    l.append(row["name"])
    l.append(row["invite_date"])
    list.append(l)

# initialises a count
count = 0
# for each row of academy
for index, row in academy.iterrows():
    # if the first one it creates a dict with name and startdate as key and value
    if count == 0:
        dict = {row["name"]: row["start_date"]}
        # increments by 1 so that dict is not redefined
        count += 1
    else:
        # if not the first timme it updates the dictionary with the name & startdate as a KVP
        app = {row["name"]: row["start_date"]}
        dict.update(app)

# for each list in the list taken from talent
for couple in list:
    # if the name is in the dict
    if couple[0] in dict:
        # and the start date is after interview date it appends the interview date to the list
        if dict[couple[0]] > couple[1]:
            couple.append(dict[couple[0]])

# converts the list of lists to a dataframe
final = pd.DataFrame(list)
# adds column names
final.columns = ["name", "int_date", "start_course"]
# drops duplicates based on name and and invited date
final = final.drop_duplicates(subset=['name', 'start_course'], keep='last')

final['start_course'] = pd.to_datetime(final['start_course'])
final['int_date'] = pd.to_datetime(final['int_date'])

# sort the values by interview date - earliest first
final = final.sort_values(["int_date"], ascending=True)
# add a unique Id
final.insert(0, 'talent_id', range(1, 1 + len(final)))



#
#
# def unique_sparta(bucket):
#     # takes in talent csvs as one and appends
#     sparta = Append_All(bucket).append_all("SpartaDays")
#     # use fix date to fix the date in the sparta table
#     sparta = fix_date(sparta, "Date")
#     return sparta
# # create instance for sparta
# sparta = unique_sparta("data7-engineering-project")
# # combine sparta and talent on the name and invite_date
# combine = pd.merge(talent, sparta,  how='outer', left_on=['name','invite_date'], right_on = ['Name','Date'])
#
#
# combine['name'] = combine['name'].fillna(combine['Name'])
# combine["Name"]= combine['Name'].fillna(combine['name'])
# combine["Date"]= combine['Date'].fillna(combine['invite_date'])
# combine["invite_date"] = combine['invite_date'].fillna(combine['Date'])
#
#
# # drops the old date
# combine = combine.drop(['Name', 'Date'], axis=1)
# # add unique ID
# combine.insert(0, 'talent_id', range(1, 1 + len(combine)))
# combine = combine.drop(combine.columns[1], axis=1)
# combine = combine.drop(combine.columns[13], axis=1)


# class Unique:
# def __init__(self, bucket):  # when creating class, input bucket name as variable
#     self.s3_client = boto3.client('s3')  # making client
#     self.bucket2 = bucket
#     self.talent = Append_All(bucket).append_all("Talent")
#     self.academy = Append_All(bucket).append_all("Academy", include_title=1)



s = Append_All("data7-engineering-project").append_all("SpartaDays")
s = fix_date(s, "Date")
s = s[["Name", "Date"]]
talent = unique_talent("data7-engineering-project")
academy = unique_course("data7-engineering-project")
# converts the date string to date time for comparison in both dataframes

# f = s.append(talent)
# final1 = f.append(academy)
