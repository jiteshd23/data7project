import boto3
# import glob


# This function takes a file and uploads it to the s3 bucket in a specified location with the desired name
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False


upload_to_aws('file_json_load.json', 'data7-engineering-project', 'Test/testing_push')


# class to push multiple files to s3 bucket, still work in progress.
# class PushMultiples():
#
#     # initialising s3 client and bucket to send files to
#     def __init__(self):
#         self.s3_client = boto3.client("s3")
#         self.buck = 'data7-engineering-project'
#
#     def upload_all(self, bucket_name, s3_filename):
#         s3 = self.s3_client
#         folder_loc = glob.glob("~/Users/tech-a41/Desktop/csv_collection")
#
#         # iterate through to grab all files in folder and upload to s3 bucket
#         for filename in folder_loc:
#             print(f"Putting filename {filename}")
#             s3.upload_file(filename, bucket_name, s3_filename)
#
#         s3.put_object(Bucket="data7-engineering-project", Key="Test/testing_multiple")
#
#
#
# x = PushMultiples()
# x.upload_all('data7-engineering-project', 'Test/testing_push')
