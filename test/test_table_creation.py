import unittest
from data7project.scripts.table_scripts.df_all import *
from data7project.scripts.table_scripts.df_performance_all import *
import pandas as pd


class TableCreationTest(unittest.TestCase):

    def test_creation(self):
        self.assertIs(type(PerformanceAll.sa_pull()),pd.DataFrame)

