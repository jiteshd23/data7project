###### FUNCTION FOR CORRECTING MISPELLINGS
from fuzzywuzzy import fuzz
# input the df and the column that needs correcting - output is the cleaned df
def mispell(df, col):
    # create an array of the values in
    arr = df[col].to_numpy()
    # initialise an empty dictionary
    dict = {}
    # loop through the list values
    for i in arr:
        # loop through list of cities
        for x in arr:
            # if the two cities match with a ratio of 80
            if fuzz.token_sort_ratio(i,x) > 80:
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
        df = df.replace(incorrect, dict[incorrect])
        # now drops the duplicates since the cities have been corrected
        df = df.drop_duplicates(col)
        # only return the column in question
        df = df[col]
        # return a sorted df
        return df.sort_values(col, ascending=True)