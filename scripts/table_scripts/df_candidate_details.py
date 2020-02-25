from data7project.scripts.pull_scripts.pull_single import PullSingle
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.scripts.clean_scripts.clean_functions import *
import pandas as pd

def clean_name(table,col):
    table_fix = table
    table_fix[col] = table_fix[col].map(lambda x: x.title)
    return table_fix

talent = Append_All("data7-engineering-project").append_all("Talent")
sdays = Append_All("data7-engineering-project").append_all("SpartaDays")
academy = Append_All("data7-engineering-project").append_all("Academy")
# interview = pd.DataFrame.from_dict(Append_All("data7-engineering-project").append_all("Interview Notes"))["name"]

talent = clean_name(talent, "name")
sdays = clean_name(sdays, "Name")
academy = clean_name(academy, "name")
print(talent.head())








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
