
###### FUNCTION FOR CORRECTING MISPELLINGS
from fuzzywuzzy import fuzz
# input the df and the column that needs correcting - output is the cleaned df
# sets ratio to 80% - can be adjusted
def mispell(df, col, ratio=80):
    # create an array of the values in the stated column
    arr = df[col].to_numpy()
    # initialise an empty dictionary
    dict = {}
    # loop through the values list
    for i in arr:
        # to compare the same list again loop through the list
        for x in arr:
            # if they are exactly the same then continue
            if i == x:
                continue
            # if the two match with a ratio of less than 80 then no correction is needed
            elif fuzz.token_sort_ratio(i,x) < ratio:
                continue
            else:
                # if first iterator is in dict
                if i in dict:
                    # update dictionary with first iterator as value and second iterator as key
                    dict.update({x:i})
                else:
                    # else update dictionary with second iterator as both key and value
                    # these both ensure that the string is corrected to the same string
                    dict.update({x:x})

    # this then uses the dictionary created to correct the incorrect string entries
    for incorrect in dict:
        # finds and replaces all incorrect entries in table
        df = df.replace(incorrect, dict[incorrect])
    # now drops the duplicates since they have been corrected
    df = df.drop_duplicates()
    return df
