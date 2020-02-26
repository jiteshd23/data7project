from data7project.scripts.pull_scripts.pull_single import PullSingle
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from data7project.scripts.pull_scripts.pull_json import PullJson
from data7project.scripts.pull_scripts.pull_txt import PullTxt
from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.scripts.clean_scripts.clean_functions import *
from data7project.tools.mispell_correct import *
import pandas as pd

def clean_name(table,col):
    table[col].map(lambda x: x.lower).map(lambda x: x.title)
    return table

# talent = Append_All("data7-engineering-project").append_all("Talent")
# sdays = Append_All("data7-engineering-project").append_all("SpartaDays")
# academy = Append_All("data7-engineering-project").append_all("Academy")
# interview = pd.DataFrame.from_dict(Append_All("data7-engineering-project").append_all("Interview Notes"))


talent = PullCsv("data7-engineering-project").pull("Talent", "April2019Applicants.csv")
sdays = PullTxt("data7-engineering-project").pull("SpartaDays", "Sparta Day 10 April 2019.txt")
academy = PullCsv("data7-engineering-project").pull("Academy","Business_24_2019-02-11.csv")


talent = mispell(clean_name(talent, "name"), "name")
sdays = mispell(clean_name(sdays, "Name"), "Name")
academy = mispell(clean_name(academy, "name"), "name")
talent = talent["name"]
sdays = sdays["Name"]
academy = academy["name"]


name = talent.append(sdays).append(academy)
# creates a frame of the series of just the cities
frame = {"name": name}
# create a dataframe for the cities
people = pd.DataFrame(frame)
# drop duplicates
people = people.drop_duplicates('name')

people.insert(0, "candidate_id", range(1, 1+len(people)))

print(people["name"].values)



def names_from_json(bucket):  # breaks down dataframe into only relevant information.
    test = PullSingle(bucket)
    return test
    print(test)
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket=bucket)
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if 'Interview Notes' in key['Key']:
            dict_list.append(test.pull('Interview Notes',key['Key'][len('Interview Notes')+1:]))
    for values in dict_list:
        for value in values['name']:
            outputs.append([value['name']])
    names = pd.DataFrame(outputs)
    names.columns = ['name']
    names = names.drop_duplicates('name')
    return names

print(names_from_json('data7-engineering-project'))


#
# # gender, inv date, dob, name email, phone, address, city, postcode, invited by, uni, degree
# # need to add course schedual id, first name, last name, sparta day id, interview id
# cand_id = Append_All("data7-engineering-project").append_all("Talent")
#
#
# # phone number needs the format changing, but in this situation are time can be better spent
# cand_id = cand_id[
#     ["id", "gender", "dob", "invited_date", "email", "phone_number", "address", "invited_by", "uni", "degree", "month"]]
#
# cand_id["invited_date"] = cand_id["invited_date"].fillna(0)
# cand_id["invited_date"] = cand_id["invited_date"].astype(int)
# cand_id["invited_date"] = cand_id["invited_date"].astype(str)
# cand_id["invite_date"] = cand_id["month"] + " " + cand_id["invited_date"]
# cand_id["invite_date"] = cand_id["invite_date"].str.strip()
# cand_id = (fix_date(cand_id, 'invite_date'))
# # print(cand_id)
#
# cand_id2 = Append_All("data7-engineering-project").append_all("SpartaDays")
#
# cand_name = cand_id2[
#     ["Name"]
# ]
# # print(cand_id2.loc[cand_id2["Name"]=="Bett"])
#
#
# # candidate = pd.concat([cand_id, cand_name], axis=1)
# # print(candidate)
#
# test = clean_name(cand_id,"name")
# print(test)
