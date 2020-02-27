from data7project.tools.func_replace_col_name_with_id_col import *
from data7project.scripts.table_scripts.df_all import *
from data7project.scripts.config_manager import *
from data7project.tools.populate_sql_script import *
from data7project.scripts.table_scripts.unique_id import *

sql_cnxn = SQLConnect(driver(),
                      server(),
                      database(),
                      username(),
                      password())

aws_cnxn = CreateAll(bucket())

unique = unique(bucket())

# SKILLS -- DONE
skill = aws_cnxn.skill()
sql_cnxn.import_sql(skill, 'skill')

# CANDIDATE_SKILLS -- DONE
candidate_skill = replace_col_with_id(aws_cnxn.candidate_skill(), skill, 'language', 'skills', 'skill_id')
candidate_skill = replace_col_with_id(candidate_skill, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(candidate_skill, 'candidate_skill')

# STRENGTH -- DONE
strength = aws_cnxn.strength()
sql_cnxn.import_sql(strength, 'strength')

# CANDIDATE_STRENGTH -- DONE
candidate_strength = replace_col_with_id(aws_cnxn.candidate_strength(), strength, 'strength', 'strengths', 'strength_id')
candidate_strength = replace_col_with_id(candidate_strength, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(candidate_strength, 'candidate_strength')

# WEAKNESS -- DONE
weakness = aws_cnxn.weakness()
sql_cnxn.import_sql(weakness, 'weakness')

#CANDIDATE WEAKNESS -- DONE
candidate_weakness = replace_col_with_id(aws_cnxn.candidate_weakness(), weakness, 'weakness', 'weaknesses', 'weakness_id')
candidate_weakness = replace_col_with_id(candidate_weakness, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(candidate_weakness, 'candidate_weakness')

# EDUCATION -- DONE
education = aws_cnxn.education()
sql_cnxn.import_sql(education, 'education')

# CITY -- DONE
city = aws_cnxn.city()
sql_cnxn.import_sql(city, 'city')

# STAFF -- DONE
staff = aws_cnxn.staff()
sql_cnxn.import_sql(staff, 'staff')

# CANDIDATE -- DONE
candidate = replace_col_with_id(aws_cnxn.candidate(), unique, 'UNID', 'UNID', 'talent_id')
candidate = replace_col_with_id(candidate, education, 'uni', 'uni', 'university_id')
candidate = replace_col_with_id(candidate, city, 'city', 'city', 'city_id')
candidate = replace_col_with_id(candidate, staff, 'invited_by', 'staff', 'staff_id', 'invited by')
sql_cnxn.import_sql(candidate, 'candidate')

# COURSE -- DONE
course = aws_cnxn.course()
sql_cnxn.import_sql(course, 'course')

# COURSE_SCHEDULE -- DONE
course_schedule = aws_cnxn.course_schedule()
course_schedule = replace_col_with_id(course_schedule, staff, 'trainer', 'staff', 'staff_id')
course_schedule = replace_col_with_id(course_schedule, course, 'course', 'course_name', 'course_name_id')
sql_cnxn.import_sql(course_schedule, 'course_schedule')

# INTERVIEW -- DONE
interview = aws_cnxn.interview()
interview = replace_col_with_id(interview, course, 'course_interest', 'course_name', 'course_name_id')
interview = replace_col_with_id(interview, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(interview, 'interview')

# PERFORMANCE -- DONE
sql_cnxn.import_sql(replace_col_with_id(aws_cnxn.intellect(), unique, 'perf_id', 'perf_id', 'talent_id'), 'intellect')
sql_cnxn.import_sql(replace_col_with_id(aws_cnxn.perserve(), unique, 'perf_id', 'perf_id', 'talent_id'), 'perserve')
sql_cnxn.import_sql(replace_col_with_id(aws_cnxn.savvy(), unique, 'perf_id', 'perf_id', 'talent_id'), 'savvy')
sql_cnxn.import_sql(replace_col_with_id(aws_cnxn.self_del(), unique, 'perf_id', 'perf_id', 'talent_id'), 'self_del')
sql_cnxn.import_sql(replace_col_with_id(aws_cnxn.stand_alone(), unique, 'perf_id', 'perf_id', 'talent_id'), 'stand_alone')
sql_cnxn.import_sql(replace_col_with_id(aws_cnxn.prob_solve(), unique, 'perf_id', 'perf_id', 'talent_id'), 'prob_solve')

