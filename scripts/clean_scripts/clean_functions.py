import dateutil.parser
import numpy as np
from dateutil.parser._parser import ParserError


def fix_date(table, col):
    table_fix = table
    table_fix[col] = table_fix[col].map(lambda x: dateutil.parser.parse(str(x)).strftime('%d/%m/%Y'), na_action='ignore')
    return table_fix

def create_dropout_col(table, nan_value=np.NaN):
    table['dropout'] = 1
    for col in table.columns[:-1]:
        table['dropout'] = np.where(table[col] == nan_value, 0, table['dropout'])
    return table


def clean_course_schedule():
    return fix_date(df_course_schedule)


def clean_interview():
    return fix_date(df_interview)

def clean_name(table,col):
    table[col] = table[col].str.title()
    return table
