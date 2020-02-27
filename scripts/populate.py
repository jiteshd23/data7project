from data7project.tools.func_replace_col_name_with_id_col import *
from data7project.scripts.table_scripts.df_all import *
from data7project.scripts.config_manager import *
from data7project.tools.populate_sql_script import *
from data7project.scripts.table_scripts.unique_id import *
from data7project.tools.df_to_cloud_as_csv import *

sql_cnxn = SQLConnect(driver(),
                      server(),
                      database(),
                      username(),
                      password())

aws_cnxn = CreateAll(bucket())

ps = Push(bucket())
unique = unique(bucket(),clean_folder())

# SKILLS -- DONE
skill = aws_cnxn.skill()
sql_cnxn.import_sql(skill, 'skill')
ps.push_to_cloud(skill)

# CANDIDATE_SKILL -- DONE
candidate_skill = replace_col_with_id(aws_cnxn.candidate_skill(), skill, 'language', 'skills', 'skill_id')
candidate_skill = replace_col_with_id(candidate_skill, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(candidate_skill, 'candidate_skill')
ps.push_to_cloud(candidate_skill)


# STRENGTH -- DONE
strength = aws_cnxn.strength()
sql_cnxn.import_sql(strength, 'strength')
ps.push_to_cloud(strength)

# CANDIDATE_STRENGTH -- DONE
candidate_strength = replace_col_with_id(aws_cnxn.candidate_strength(), strength, 'strength', 'strengths', 'strength_id')
candidate_strength = replace_col_with_id(candidate_strength, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(candidate_strength, 'candidate_strength')
ps.push_to_cloud(candidate_strength)

# WEAKNESS -- DONE
weakness = aws_cnxn.weakness()
sql_cnxn.import_sql(weakness, 'weakness')
ps.push_to_cloud(weakness)

#CANDIDATE WEAKNESS -- DONE
candidate_weakness = replace_col_with_id(aws_cnxn.candidate_weakness(), weakness, 'weakness', 'weaknesses', 'weakness_id')
candidate_weakness = replace_col_with_id(candidate_weakness, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(candidate_weakness, 'candidate_weakness')
ps.push_to_cloud(candidate_weakness)

# EDUCATION -- DONE
education = aws_cnxn.education()
sql_cnxn.import_sql(education, 'education')
ps.push_to_cloud(education)

# CITY -- DONE
city = aws_cnxn.city()
sql_cnxn.import_sql(city, 'city')
ps.push_to_cloud(city)

# STAFF -- DONE
staff = aws_cnxn.staff()
sql_cnxn.import_sql(staff, 'staff')
ps.push_to_cloud(staff)

# CANDIDATE -- DONE
candidate = replace_col_with_id(aws_cnxn.candidate(), unique, 'UNID', 'UNID', 'talent_id')
candidate = replace_col_with_id(candidate, education, 'uni', 'uni', 'university_id')
candidate = replace_col_with_id(candidate, city, 'city', 'city', 'city_id')
candidate = replace_col_with_id(candidate, staff, 'invited_by', 'staff', 'staff_id', 'invited by')
sql_cnxn.import_sql(candidate, 'candidate')
ps.push_to_cloud(candidate)

# COURSE -- DONE
course = aws_cnxn.course()
sql_cnxn.import_sql(course, 'course')
ps.push_to_cloud(course)

# COURSE_SCHEDULE -- DONE
course_schedule = aws_cnxn.course_schedule()
course_schedule = replace_col_with_id(course_schedule, staff, 'trainer', 'staff', 'staff_id')
course_schedule = replace_col_with_id(course_schedule, course, 'course', 'course_name', 'course_name_id')
sql_cnxn.import_sql(course_schedule, 'course_schedule')
ps.push_to_cloud(course_schedule)

# INTERVIEW -- DONE
interview = aws_cnxn.interview()
interview = replace_col_with_id(interview, course, 'course_interest', 'course_name', 'course_name_id')
interview = replace_col_with_id(interview, unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(interview, 'interview')
ps.push_to_cloud(interview)

# PERFORMANCE -- DONE
intellect = replace_col_with_id(aws_cnxn.intellect(), unique, 'perf_id', 'perf_id', 'talent_id')
sql_cnxn.import_sql(intellect, 'intellect')
ps.push_to_cloud(intellect)

perserve = replace_col_with_id(aws_cnxn.perserve(), unique, 'perf_id', 'perf_id', 'talent_id')
sql_cnxn.import_sql(perserve, 'perserve')
ps.push_to_cloud(perserve)

savvy = replace_col_with_id(aws_cnxn.savvy(), unique, 'perf_id', 'perf_id', 'talent_id')
sql_cnxn.import_sql(savvy, 'savvy')
ps.push_to_cloud(savvy)

self_del = replace_col_with_id(aws_cnxn.self_del(), unique, 'perf_id', 'perf_id', 'talent_id')
sql_cnxn.import_sql(self_del, 'self_del')
ps.push_to_cloud(self_del)

stand_alone = replace_col_with_id(aws_cnxn.stand_alone(), unique, 'perf_id', 'perf_id', 'talent_id')
sql_cnxn.import_sql(stand_alone, 'stand_alone')
ps.push_to_cloud(stand_alone)

prob_solve = replace_col_with_id(aws_cnxn.prob_solve(), unique, 'perf_id', 'perf_id', 'talent_id')
sql_cnxn.import_sql(prob_solve, 'prob_solve')
ps.push_to_cloud(prob_solve)

# SPARTA_DAYS  = DONE

sparta_days = replace_col_with_id(aws_cnxn.sparta_days(), unique, 'UNID', 'UNID', 'talent_id')
sql_cnxn.import_sql(sparta_days, 'sparta_days')
ps.push_to_cloud(sparta_days)



