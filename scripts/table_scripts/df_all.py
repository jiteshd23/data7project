from data7project.scripts.table_scripts.df_address import *
from data7project.scripts.table_scripts.df_candidate_details import *
from data7project.scripts.table_scripts.df_candidate_skills import *
from data7project.scripts.table_scripts.df_candidate_strengths import *
from data7project.scripts.table_scripts.df_candidate_weaknesses import *
from data7project.scripts.table_scripts.df_city import *
from data7project.scripts.table_scripts.df_course_schedule import *
from data7project.scripts.table_scripts.df_education import *
from data7project.scripts.table_scripts.df_interview import *
from data7project.scripts.table_scripts.df_performance_all import *
from data7project.scripts.table_scripts.df_performance_all import *
from data7project.scripts.table_scripts.df_skills_list import *
from data7project.scripts.table_scripts.df_staff import *
from data7project.tools import *

#generates the final table
class CreateAll:
    def __init__(self, bucket):
        self._bucket = bucket
        self._performance_bucket = PerformanceAll(bucket)

    def intellect(self):
        return self._performance_bucket.ih_pull()

    def savvy(self):
        return self._performance_bucket.ih_pull()

    def perserve(self):
        return self._performance_bucket.pv_pull()

    def self_del(self):
        return self._performance_bucket.sd_pull()

    def stand_alone(self):
        return self._performance_bucket.sa_pull()

    def prob_solve(self):
        return self._performance_bucket.ps_pull()

    def address(self):
        return address(self._bucket)

    def candidate_skill(self):
        return make_c_skills(self._bucket)

    def candidate_strength(self):
        return make_c_strengths(self._bucket)

    def candidate_weakness(self):
        return make_c_weakness(self._bucket)

    def city(self):
        return city_table(self._bucket)

    def course_schedule(self):
        return course_schedule(self._bucket)