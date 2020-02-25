import boto3
import unittest
from moto import mock_s3
from ..test.test_files.mock_push import upload_to_aws

class PushFile(unittest.TestCase):

    def test_push(self):
        pass