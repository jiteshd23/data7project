# import the pullcsv tool
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from fuzzywuzzy import fuzz
university = PullCsv("data7-engineering-project").pull("Talent", "April2019Applicants.csv")
# drops all duplicates of city and removes na values (for purpose of creating the city id table)
university = university.drop_duplicates('uni').dropna()
# lists the cities  to generate a list of all cities in table
arr = university["uni"].to_numpy()
# initialise an empty dictionary
dict = {}
# loop through the list of cities
for i in arr:
    # loop through list of cities
    for x in arr:
        # if the two cities match with a ratio of 80
        if fuzz.token_sort_ratio(i,x) > 60:
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
    university = university.replace(incorrect, dict[incorrect])
    # now drops the duplicates since the cities have been corrected
    university = university.drop_duplicates('uni')

uni = (university["uni"])