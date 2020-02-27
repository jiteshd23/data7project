import unittest
from data7project.scripts.pull_scripts.pull_single import PullSingle
import pandas as pd


class PullAllTest(unittest.TestCase):

    # unit test to check if specific column names are in these file types
    def test_all(self):
        self.bucket = PullSingle(bucket="data7-engineering-project")
        self.assertIn('name', self.bucket.pull("Interview Notes", "11329.json"))
        self.assertIn('name', self.bucket.pull("Talent", "April2019Applicants.csv"))
        self.assertIn('Name', self.bucket.pull("SpartaDays", "Sparta Day 1 August 2019.txt"))

    # unit testing to see if a json file is returned
    def test_json(self):
        self.bucket = PullSingle(bucket="data7-engineering-project")
        self.assertTrue(self.bucket.pull("Interview Notes", "11329.json"))

    # unit testing to see if the pulled csv file is a dataframe object
    def test_csv(self):
        self.bucket = PullSingle(bucket="data7-engineering-project")
        self.assertIs(type(self.bucket.pull("Talent", "April2019Applicants.csv")), pd.DataFrame)

    # unit testing to see if the pulled txt file is a dataframe object
    def test_text(self):
        self.bucket = PullSingle(bucket="data7-engineering-project")
        self.assertIs(type(self.bucket.pull("SpartaDays", "Sparta Day 1 August 2019.txt")), pd.DataFrame)


