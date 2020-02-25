# OUTPUTS a df with just the distinct University names
# - uses the appendall tool to pull in a generate a full csv with all files in that format
#
# import the appending tool
from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from fuzzywuzzy import fuzz
def df_educate(bucket, folder):
    # generate a df with all csvs for talent using the append all tool
    university = Append_All(bucket).append_all(folder)
    # drops all duplicates of uni and removes na values (for purpose of creating the uni id table)
    university = university.drop_duplicates('uni').dropna()
    # lists the cities  to generate a list of all unis in table
    arr = university["uni"].to_numpy()
    # initialise an empty dictionary
    dict = {}
    # loop through the list of uni
    for i in arr:
        # loop through list of unis
        for x in arr:
            if i == x:
                continue
            else: # if the two unis match with a ratio of 70
                if fuzz.token_sort_ratio(i,x) > 70:
                    # if first iterator is in dict
                    if i in dict:
                        # update dictionary with first iterator as key and second iterator as value
                        dict.update({i:i})
                    else:
                        # else update dictionary with first iterator as value and second iterator as key
                        dict.update({x:i})
                else:
                    if i in dict:
                        # if first iterator is a key in dict it continues the loop and does nothing
                        continue
                    else:
                        if i in dict.values():
                            # if first iterator is a value in dict it continues the loop and does nothing
                            continue
                        else:
                            # else it updates the dictionary with first iterator as key and second iterator as value
                            dict.update({i:x})
    # this then uses the dictionary to correct the unis
    for incorrect in dict:
        # finds and replaces all incorrect entries in table
        university = university.replace(incorrect, dict[incorrect])
        # now drops the duplicates since the unis have been corrected
        university = university.drop_duplicates('uni')

    return university["uni"]
