from data7project.scripts.table_scripts.tools.append_tables_buckets import *
import pandas as pd

def unique_candidate(bucket):
    test = PullSingle(bucket)
    folder = "Interview Notes"
    _s3_client = boto3.client("s3")
    contents = _s3_client.list_objects(Bucket=bucket)
    dict_list = []
    outputs = []
    for key in contents['Contents']:
        if folder in key['Key']:
            dict_list.append(test.pull(folder, key['Key'][len(folder) + 1:]))
    for value in dict_list:
        n_list = [value['name'], value['date']]
        outputs.append(n_list)
    out = pd.DataFrame(outputs)
    out.columns = ['name', 'date']

    return out


print(unique_candidate("data7-engineering-project"))
