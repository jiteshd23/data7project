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


# skill = aws_cnxn.skill()
# print(skill)

# candidate_skill = replace_col_with_id(aws_cnxn.candidate_skill(), skill, 'language', 'skills', 'skill_id')

# print(candidate_skill)

# strength = aws_cnxn.strength()
# print(strength)
# candidate_strength = replace_col_with_id(aws_cnxn.candidate_strength(), strength, 'strength', 'strengths', 'strength_id')
#
# print(candidate_strength)

# weakness = aws_cnxn.weakness()
# print(weakness)
# candidate_weakness = replace_col_with_id(aws_cnxn.candidate_weakness(), weakness, 'weakness', 'weaknesses', 'weakness_id')
# print(candidate_weakness)






