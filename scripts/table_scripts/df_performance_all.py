from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.tools.mispell_correct import *

""" This is the creation of the performance tables, where the data will be split by rubrick and contained in different 
tables.
performanceAll is a class that will take all the files from the academy bucket and clean the names of the students 
simultaneously, split by rubrick and append onto its individual dataframe """
class PerformanceAll:
    def __init__(self, bucket):
        self._appended_acad_df = mispell(Append_All(bucket).append_all('Academy'), 'name')

    def ih_pull(self):
        ih_pull = self._appended_acad_df.filter(
            ["name", "IH_W1", "IH_W2", "IH_W3", "IH_W4", "IH_W5", "IH_W6", "IH_W7", "IH_W8", "IH_W9", "IH_W10"])
        return ih_pull

    def is_pull(self):
        is_pull = self._appended_acad_df.filter(
            ["name", "IS_W1", "IS_W2", "IS_W3", "IS_W4", "IS_W5", "IS_W6", "IS_W7", "IS_W8", "IS_W9", "IS_W10"])
        return is_pull

    def pv_pull(self):
        pv_pull = self._appended_acad_df.filter(
            ["name", "PV_W1", "PV_W2", "PV_W3", "PV_W4", "PV_W5", "PV_W6", "PV_W7", "PV_W8", "PV_W9", "PV_W10"])
        return pv_pull

    def ps_pull(self):
        ps_pull = self._appended_acad_df.filter(
            ["name", "PS_W1", "PS_W2", "PS_W3", "PS_W4", "PS_W5", "PS_W6", "PS_W7", "PS_W8", "PS_W9", "PS_W10"])
        return ps_pull

    def sd_pull(self):
        sd_pull = self._appended_acad_df.filter(
            ["name", "SD_W1", "SD_W2", "SD_W3", "SD_W4", "SD_W5", "SD_W6", "SD_W7", "SD_W8", "SD_W9", "SD_W10"])
        return sd_pull

    def sa_pull(self):
        sa_pull = self._appended_acad_df.filter(
            ["name", "SA_W1", "SA_W2", "SA_W3", "SA_W4", "SA_W5", "SA_W6", "SA_W7", "SA_W8", "SA_W9", "SA_W10"])
        return sa_pull

print(PerformanceAll('data7-engineering-project').sd_pull())