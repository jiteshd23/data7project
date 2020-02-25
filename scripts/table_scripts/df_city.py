# THIS INPUTS the bucket and folder for the csvs where the cities are held
# OUTPUTS an order csv with the list of the distinct cities
from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from fuzzywuzzy import fuzz

def city_table(bucket, folder):
    # sets up the df using append all tool
    cities = Append_All(bucket).append_all(folder)
    # drops all duplicates of city and removes na values (for purpose of creating the city id table)
    cities = cities.drop_duplicates('city').dropna()
    # lists the cities  to generate a list of all cities in table
    arr = cities["city"].to_numpy()
    # initialise an empty dictionary
    dict = {}
    # loop through the list of cities
    for i in arr:
        # loop through list of cities
        for x in arr:
            # if the two cities match with a ratio of 80
            if fuzz.token_sort_ratio(i,x) > 95:
                # if first iterator is in dict
                if i in dict:
                    # update dictionary with first iterator as key and second iterator as value
                    dict.update({i:x})
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
    # this then uses the dictionary to correct the cities
    for incorrect in dict:
        # finds and replaces all incorrect entries in table
        cities = cities.replace(incorrect, dict[incorrect])
        # now drops the duplicates since the cities have been corrected
        cities = cities.drop_duplicates('city')

    # orders the table returns only the cities
    cities = cities["city"]
    return cities.sort_values('city', ascending=True)
