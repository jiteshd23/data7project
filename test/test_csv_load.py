import unittest
from data7project.scripts.pull_scripts.pull_csv import PullCsv


class CsvTest(unittest.TestCase):

    #  tests the PullCsv class, raises an Assertion error if the file that is pulled is not a csv
    def test_csv(self):
        try:
            x = PullCsv("data7-engineering-project")
            x = x.pull("Talent", "April2019Applicants.csv")
            return x
        except Exception:
            raise AssertionError('CSV file not found')


