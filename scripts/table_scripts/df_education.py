# INPUTS A BUCKET AND FOLDER
# OUTPUTS a df with just the distinct University names
# NOTE THAT THIS COULD DO WITH SOME ADDITIONAL CLEANING TO STANDARDISE UNI NAMES

from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.tools.mispell_tool import *
import pandas as pd

def df_educate(bucket, folder):
    # generate a df with all csvs for talent using the append all tool
    university = Append_All(bucket).append_all(folder)
    # drops all duplicates of uni and removes na values (for purpose of creating the uni id table)
    university = university.drop_duplicates('uni').dropna()
    # corrects any slight mispelliing of uni names - use 70% matching
    university = mispell(university, "uni", ratio=70)
    # creates a frame of the series of just the unis
    frame = {"uni": university["uni"]}
    # create a dataframe for the unis
    university = pd.DataFrame(frame)
    # drop duplicates
    university = university.drop_duplicates('uni')
    # returns an ordered list of unique unis from all csvs
    return university.sort_values('uni', ascending=True)
