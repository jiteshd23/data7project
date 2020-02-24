import boto3
import pandas as pd


# setting the init for the class
class PullTxt:
    def __init__(self, bucket):
        self._s3_client = boto3.client("s3")
        self._bucket = bucket

    # pull file method
    def pull(self, folder, file):

        # setting the bucket as folder and file for scalability, and decoding the data so it is more usable
        file = self._s3_client.get_object(Bucket=self._bucket, Key=folder + "/" + file)
        file = file['Body'].read()
        file = file.decode('utf-8')

        # splits each line into a list
        file_list = file.splitlines()

        # taking data, as it was on the top row
        date = file_list[0]

        # taking the location the same way
        location = file_list[1]

        # the bulk of the data started from this point to the end, so each line is now a list
        file_list_data = file_list[3:]

        data_list = []
        # making a for loop that splits each row into a list of lists
        for line in file_list_data:
            name = line[:line.find('-') - 1]
            psychometrics = line[
                            line.find('Psychometrics: ') + len('Psychometrics: '):line.find('/', line.find(
                                'Psychometrics: '))]
            presentation = line[
                           line.find('Presentation: ') + len('Presentation: '):line.find('/',
                                                                                         line.find('Presentation: '))]
            # appending the list of lists into one
            data_list.append([name, psychometrics, presentation, date, location])

        # making the dafeframe

        pd_columns = ['Name', 'Psychometrics', 'Presentation', 'Date', 'Location']
        pd_format = pd.DataFrame(data_list, columns=pd_columns)
        return pd_format

