from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.scripts.clean_scripts.clean_functions import *

""" This is the creation of the performance tables, where the data will be split by rubrick and contained in different 
tables.
performanceAll is a class that will take all the files from the academy bucket and clean the names of the students 
simultaneously, split by rubrick and append onto its individual dataframe """


# to merge on name and 2+ scores. date is in the file title, we know how to do it but are pressed for time
class PerformanceAll:
    def __init__(self, bucket):
        self._appended_acad_df = Append_All(bucket).append_all('Academy', include_title=1)
        # new data frame with split value columns on the underscore
        new = self._appended_acad_df["title"].str.split("_", n=2, expand=True)
        # making separate course name column from new data frame
        self._appended_acad_df["course"] = new[0]
        # making separate course name column from new data frame
        self._appended_acad_df["course_number"] = new[1]
        # making separate start date column from new data frame
        self._appended_acad_df["start_date"] = new[2]
        # Dropping old title columns
        self._appended_acad_df.drop(columns=["title"], inplace=True)
        # remove .csv from the filename in the start_date column
        self._appended_acad_df["start_date"] = self._appended_acad_df["start_date"].str.replace('.csv', '')
        self._appended_acad_df = fix_date(self._appended_acad_df, "start_date")
        # returns an ordered list of unique courses from all csvs using course and course number
        self._appended_acad_df = self._appended_acad_df.sort_values(['course', "course_number"], ascending=True)
        # # returns only name and start_date
        # self._appended_acad_df = self._appended_acad_df[["name", "start_date"]]
        self._appended_acad_df["perf_id"] = self._appended_acad_df["name"] + self._appended_acad_df["start_date"]

    def ih_pull(self):
        ih_pull = self._appended_acad_df.filter(
            ["name", "start_date", "perf_id","IH_W1", "IH_W2", "IH_W3", "IH_W4", "IH_W5", "IH_W6", "IH_W7", "IH_W8", "IH_W9",
             "IH_W10"])
        return clean_name(ih_pull, "name")

    def is_pull(self):
        is_pull = self._appended_acad_df.filter(
            ["name", "start_date", "perf_id", "IS_W1", "IS_W2", "IS_W3", "IS_W4", "IS_W5", "IS_W6", "IS_W7", "IS_W8", "IS_W9",
             "IS_W10"])
        return clean_name(is_pull, "name")

    def pv_pull(self):
        pv_pull = self._appended_acad_df.filter(
            ["name", "start_date",  "perf_id","PV_W1", "PV_W2", "PV_W3", "PV_W4", "PV_W5", "PV_W6", "PV_W7", "PV_W8", "PV_W9",
             "PV_W10"])
        return clean_name(pv_pull, "name")

    def ps_pull(self):
        ps_pull = self._appended_acad_df.filter(
            ["name", "start_date", "perf_id", "PS_W1", "PS_W2", "PS_W3", "PS_W4", "PS_W5", "PS_W6", "PS_W7", "PS_W8", "PS_W9",
             "PS_W10"])
        return clean_name(ps_pull, "name")

    def sd_pull(self):
        sd_pull = self._appended_acad_df.filter(
            ["name", "start_date",  "perf_id","SD_W1", "SD_W2", "SD_W3", "SD_W4", "SD_W5", "SD_W6", "SD_W7", "SD_W8", "SD_W9",
             "SD_W10"])
        return clean_name(sd_pull, "name")

    def sa_pull(self):
        sa_pull = self._appended_acad_df.filter(
            ["name", "start_date",  "perf_id","SA_W1", "SA_W2", "SA_W3", "SA_W4", "SA_W5", "SA_W6", "SA_W7", "SA_W8", "SA_W9",
             "SA_W10"])
        return clean_name(sa_pull, "name")

