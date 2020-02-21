import pytest
import unittest
import os
import os.path
import json
from data7project.scripts.pull_scripts.pull_json import PullJson

json_pull = PullJson


class JsonTest(unittest.TestCase):

    # check file can be loaded from aws s3 bucket
    def test_dict(self):
        try:
            x = json_pull("data7-engineering-project")
            x = x.pull("Interview Notes", "11329.json")
            print(x)
        except Exception:
            raise AssertionError('Not in JSON format')
