import pytest
import unittest
import os
import os.path
import json


class JsonTest(unittest.TestCase):
    dictionary = {'name': 'tamur', 'gender': 'male'}

    # check file is in a dictionary format
    def test_dict(self):
        for key, value in self.dictionary.items():
            assert key, value

    # check file is in a json format
    def test_dictttt(self):

        try:
            json.load(open('/Users/Tech-A41/Data7proj/data7project/test.json'))
        except Exception:
            raise AssertionError('Not in JSON format')

        # try:
        #     if json.dumps(self.filename):
        #         return
        # except:
        #     print('no')
