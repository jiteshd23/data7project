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



# NOT WORKING YET
# def upload_all(csv_file_loc,bucket_name, s3_filename):
#     s3 = boto3.client('s3')
#     bucket_name = 'data7-engineering-project'
#     csv_file_loc = glob.glob("~/Users/tech-a41/Desktop/csv_collection")
#
#     for filename in csv_file_loc:
#         print("Putting %s" % filename)
#         s3.upload_file(filename, bucket_name, s3_filename)
#
#     s3.put_object(Key="Test/testing_multi", Body=csv_file_loc)
#
#
# upload = upload_all('data7-engineering-project', 'Test/testing')
