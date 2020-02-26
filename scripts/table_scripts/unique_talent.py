from data7project.scripts.pull_scripts.pull_single import PullSingle
from data7project.scripts.pull_scripts.pull_csv import PullCsv
from data7project.scripts.pull_scripts.pull_json import PullJson
from data7project.scripts.pull_scripts.pull_txt import PullTxt
from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.scripts.clean_scripts.clean_functions import *
from data7project.tools.mispell_correct import *
import pandas as pd
from functools import reduce

talent = Append_All("data7-engineering-project").append_all("Talent")
print(talent.head())