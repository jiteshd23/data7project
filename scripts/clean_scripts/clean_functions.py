import dateutil.parser
import numpy as np


def fix_date(table):
    for col in table.columns:
        try:
            dateutil.parser.parse(table[col][0])
            table[col] = table[col].map(lambda x: dateutil.parser.parse(x).strftime('%d/%m/%Y'))
        except:
            continue
    return table


def create_dropout_col(table, nan_value=np.NaN):
    table['dropout'] = 1
    for col in table.columns[:-1]:
        table['dropout'] = np.where(table[col] == nan_value, 0, table['dropout'])
    return table


def clean_course_schedule():
    return fix_date(df_course_schedule)


def clean_interview():
    return fix_date(df_interview)
