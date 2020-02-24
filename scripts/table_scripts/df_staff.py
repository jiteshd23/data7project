
# import the pullcsv tool
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from fuzzywuzzy import fuzz


academy = PullCsv("data7-engineering-project").pull("Academy", "Data_66_2019-12-02.csv")
applic = PullCsv("data7-engineering-project").pull("Talent", "April2019Applicants.csv")

## CURRENTLY WORKS WITH JUST A SINGLE INSTANCE OF EACH CSV - This can be adapted to take in the full dataframes

#### this converts the academy table and the applicants table to a staff pandas dataframe
# drop duplicates based on trainer in the academy df and drop NaN values
academy = academy.drop_duplicates('trainer').dropna()
# add an emptype column with trainer
academy["emp_type"] = "trainer"
# return only the trainer and emptype columns
academy = academy[['trainer','emp_type']]
# rename the column for trainer to staff
academy.rename(columns={'trainer':'staff'}, inplace=True)
# drop duplicates based on invited by in the applicants df and drop NaN values
applic = applic.drop_duplicates('invited_by').dropna()
# add an emptype column with talent
applic["emp_type"] = "talent"
# return only the invited by and emptype columns
applic = applic[['invited_by','emp_type']]
# rename the column for invitedby to staff
applic.rename(columns={'invited_by':'staff'}, inplace=True)
# appends the applic and academy tables to generate all staff
staff = academy.append(applic)
staff1 = academy.append(applic)

# lists the staff names to generate a list of all stafff
arr = staff["staff"].to_numpy()
# initialise an empty dictionary
dict = {}
# loop through the list of staff names
for i in arr:
    # loop through list of staff names
    for x in arr:
        # if the two names match with a ratio of 80
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
# this then uses the dictionary to correct the names
for incorrect in dict:
    # finds and replaces all incorrect entries in table
    staff = staff.replace(incorrect, dict[incorrect])
    # now drops the duplicates since the names have been corrected
    staff = staff.drop_duplicates('staff')


print(staff)
