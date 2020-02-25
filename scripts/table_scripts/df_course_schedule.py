####WORK IN PROGRESSS
from data7project.scripts.table_scripts.tools.append_tables_buckets import *

def course_schedule(bucket, folder):
    academy = Append_All(bucket).append_all(folder, include_title=1)
    # drop duplicates of the title and trainer (THIS SHOULD BE ONLY ONE ROW PER FILE)
    course_s = academy.drop_duplicates(["title", "trainer"])
    # reduce the dataframe that is being worked with to just title and trainer
    course_s = course_s[['title','trainer']]
    # new data frame with split value columns on the underscore
    new = course_s["title"].str.split("_", n=2, expand=True)
    # making separate course name column from new data frame
    course_s["course"] = new[0]
    # making separate course name column from new data frame
    course_s["course_number"] = new[1]
    # making separate start date column from new data frame
    course_s["start_date"] = new[2]
    # Dropping old title columns
    course_s.drop(columns=["title"], inplace=True)
    # remove .csv from the filename in the start_date column
    course_s["start_date"] = course_s["start_date"].str.replace('.csv', '')

    # calculate the week length of the course
    a = academy.fillna("END")
    # calculating proportion of "END" in the final week 10 - if it is all "END" then the course was 8 week long
    # initialise count
    count = 0
    # create a list to iterate through of the week 10 scores
    list = a.columns[-7:-1:]
    # iterate through the list
    for i in list:
        # summate the instances of the word END in each column
        count += a[i].str.count("END").sum()
    # calculate the rows in the entry
    z = len(a.values)
    # calculate the total number of "cells" in  week 10 given the initial student number
    total = z * len(list)
    return course_s

p = course_schedule("data7-engineering-project", "Academy")
print(p)