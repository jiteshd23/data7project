from data7project.tools.func_replace_col_name_with_id_col import *
from data7project.scripts.table_scripts.df_all import *
from data7project.scripts.config_manager import *
from data7project.tools.populate_sql_script import *

sql_cnxn = SQLConnect(driver(),
                  server(),
                  'AWS_test',
                  username(),
                  password())

aws_cnxn = CreateAll(bucket())


skill = aws_cnxn.skill()
sql_cnxn.import_sql(skill, 'skill')

candidate_skill = replace_col_with_id(aws_cnxn.candidate_skill(), skill, 'language', 'skills', 'skill_id')
sql_cnxn.import_sql(candidate_skill,'candidate_skill')

strength = aws_cnxn.strength()
sql_cnxn.import_sql(strength,'strength')

candidate_strength = replace_col_with_id(aws_cnxn.candidate_strength(), strength, 'strength', 'strengths', 'strength_id')
sql_cnxn.import_sql(candidate_strength,'candidate_strength')


weakness = aws_cnxn.weakness()
sql_cnxn.import_sql(weakness,'weakness')

candidate_weakness = replace_col_with_id(aws_cnxn.candidate_weakness(), weakness, 'weakness', 'weaknesses', 'weakness_id')
sql_cnxn.import_sql(candidate_weakness,'candidate_weakness')

sql_cnxn.import_sql(aws_cnxn.address(), 'address')
sql_cnxn.import_sql(aws_cnxn.city(), 'city')
sql_cnxn.import_sql(aws_cnxn.education(), 'education')
sql_cnxn.import_sql(aws_cnxn.intellect(), 'intellect')
sql_cnxn.import_sql(aws_cnxn.savvy(), 'savvy')
sql_cnxn.import_sql(aws_cnxn.perserve(), 'perserve')
sql_cnxn.import_sql(aws_cnxn.self_del(), 'self_del')
sql_cnxn.import_sql(aws_cnxn.stand_alone(), 'stand_alone')
sql_cnxn.import_sql(aws_cnxn.prob_solve(), 'prob_solve')
sql_cnxn.import_sql(aws_cnxn.staff(), 'staff')




