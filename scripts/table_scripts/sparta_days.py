from data7project.scripts.table_scripts.tools.append_tables_buckets import *
from data7project.scripts.clean_scripts.clean_functions import *

def sparta_days(bucket):
    df = Append_All(bucket).append_all('SpartaDays')
    df = fix_date(df, 'Date')
    df['UNID'] = df['Name'] + df['Date']
    df = df[['UNID', 'Psychometrics', 'Presentation', 'Location']]
    return df

