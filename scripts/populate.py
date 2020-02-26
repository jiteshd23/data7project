from data7project.tools.func_replace_col_name_with_id_col import *
from data7project.scripts.table_scripts.df_all import *
from data7project.scripts.config_manager import *
from data7project.tools.populate_sql_script import *

sql_cnxn = SQLConnect(driver(),
                  server(),
                  database(),
                  username(),
                  password())

aws_cnxn = CreateAll(bucket())

print(aws_cnxn.address())

