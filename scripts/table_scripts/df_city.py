from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.tools.mispell_tool import *
import pandas as pd

# INPUTS the bucket and folder for the csvs where the cities are held

def city_table(bucket):
    folder = 'Talent'
    # sets up the df using append all tool
    cities = Append_All(bucket).append_all(folder)
    # drops all duplicates of city and removes na values (for purpose of creating the city id table)
    cities = cities.drop_duplicates('city').dropna()
    # corrects any slight mispelliing of city names - use 70% matching
    cities = mispell(cities, "city", ratio=70)
    # creates a frame of the series of just the cities
    frame = {"city": cities["city"]}
    # create a dataframe for the cities
    cities = pd.DataFrame(frame)
    # drop duplicates
    cities = cities.drop_duplicates('city')
    # returns an ordered list of unique cities from all csvs
    return cities.sort_values('city', ascending=True)