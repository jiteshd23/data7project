# This tool will use the pull_single tool to bring in all files of a certain format from a given bucket.
# it then appends these so that ALL files in the bucket are appended in one pandas df
import boto3
# import the PullSingle tool
from data7project.scripts.pull_scripts.pull_single import PullSingle

class Append_All:
    def __init__(self, bucket):
    # initialise the data by utilising the PullSingle class
        self.data = PullSingle(bucket)
    # create an instance of an S3 resource
        self.s3 = boto3.resource("s3")
    # create an instance of the Bucket
        self.my_bucket = self.s3.Bucket(bucket)

    def append_all(self, folder):
        # initialise a count
        count = 0
        # initialise an empty list
        a_files = []
        # append the file names to the txt_files list
        for object_summary in self.my_bucket.objects.filter(Prefix=folder + "/"):
            file_name = object_summary.key.split("/")[1] # splits on the / to give just file name
            # ignore the DS Store
            if ".DS_Store" in file_name:
                continue
            else:
                # this then appends the file name to the a_files list
                a_files.append(file_name)
# iterate through the list of a_files, pull each as a df and append to previous
        for file in a_files:
            if count == 0:
                df = self.data.pull(folder, file)  # run the .pull method to bring data into df format for first instance (count ==0)
                count +=1  # increment count to ensure the df is not changed at the start of every iteration
            else:
                sparta_days = df.append(self.data.pull(folder, file))  # append to existing df if not first iteration
        return sparta_days

