####WORK IN PROGRESSS
# import the pullcsv tool
from data7project.scripts.pull_scripts.pull_single import PullSingle
import pandas as pd

academy = PullSingle("data7-engineering-project").pull("Academy", "Data_66_2019-12-02.csv", include_title=1)
a = academy.fillna("END")
# drop duplicates of the title and trainer (THIS SHOULD BE ONLY ONE ROW PER FILE)
academy = academy.drop_duplicates(["title", "trainer"])
# reduce the dataframe that is being worked with to just title and trainer
academy = academy[['title','trainer']]
# new data frame with split value columns on the underscore
new = academy["title"].str.split("_", n=2, expand=True)
# making separate course name column from new data frame
academy["course"] = new[0]
# making separate course name column from new data frame
academy["course_number"] = new[1]
# making separate start date column from new data frame
academy["start_date"] = new[2]
# Dropping old title columns
academy.drop(columns=["title"], inplace=True)
# remove .csv from the filename in the start_date column
academy["start_date"] = academy["start_date"].str.replace('.csv', '')

count = 0
list = a.columns[-7:-1:]
print(list)
for i in list:
    if a[i].str.contains('END').any():
        count =+ 1
print(count)