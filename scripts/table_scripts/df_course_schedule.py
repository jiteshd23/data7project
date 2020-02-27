from data7project.scripts.table_scripts.tools.append_tables_buckets import *

# INPUT bucket & academy CSVs
# OUTPUT the academy CSVs and then returns a distinct list of the trainer, the course name, the course number and start date

def course_schedule(bucket):
    folder = 'Academy'
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
    # returns an ordered list of unique courses from all csvs using course and course number
    course_s = course_s.sort_values(['course', "course_number"], ascending=True)
    # add a unique Id
    course_s.insert(0, 'course_schedule_id', range(1, 1 + len(course_s)))

    # return the dataframe
    return course_s
