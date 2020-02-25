# this is ultimately will input bucket and output a list of the course names with associated week duration
from data7project.scripts.table_scripts.tools.append_tables_buckets import *
import pandas as pd
import numpy as np

# THIS FUNCTION IS A WORK IN PROGRESS - The course name and length is detailed explicity below
def courses(bucket, folder):
    courses = Append_All(bucket).append_all(folder, include_title=1)
    # calculate the week length of the course
    courses = courses.fillna("END")
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

# EXPLICITLY outline course lengths in essence of time initially
course_names = pd.DataFrame(np.array([["Business", 8], ["Data", 8], ["Engineering", 10]]), columns=["course_name", "course_length"])

