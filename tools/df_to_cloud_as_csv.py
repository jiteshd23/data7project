#PUSH TO CSV CLASS
# INPUT to class is the bucket
#  the input to the method is the df that needs to be saved as a csv and ultimately in the cloud
# & the folder /"Directory" of the saved csv within the bucket

from io import StringIO
import boto3
class Push:
    def __init__(self, bucket, folder):  # when creating class, input bucket name as variable
        self.s3_resource = boto3.resource('s3')  # making resource
        self.bucket2 = bucket #instance of the bucket
        self.folder = folder

# method to push a df to a "folder" location within the initialised bucket as a CSV file
    def push_to_cloud(self, df):
        # initialise the stringIO
        csv_buffer = StringIO()
        # save df to csv
        df.to_csv(csv_buffer)
        # generate file_n as the name of the df
        file_n = [x for x in globals() if globals()[x] is df][0]
        # make filename a csv string
        file_name = file_n + ".csv"
        # use resource to push the csv file back into the initialised bucket
        self.s3_resource.Object(self.bucket2, self.folder + "/" + file_name).put(Body=csv_buffer.getvalue())