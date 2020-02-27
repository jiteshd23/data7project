from data7project.scripts.table_scripts.tools.append_tables_buckets import *

def staff(bucket):
    # sets up the dfs for use using append all tool
    academy = Append_All(bucket).append_all("Academy")
    applic = Append_All(bucket).append_all("Talent")

    # drop duplicates based on trainer in the academy df and drop NaN values
    academy = academy.drop_duplicates('trainer')
    # add an emptype column with trainer
    academy["emp_type"] = "trainer"
    # return only the trainer and emptype columns
    academy = academy[['trainer','emp_type']]
    # rename the column for trainer to staff
    academy.rename(columns={'trainer':'staff'}, inplace=True)
    # drop duplicates based on invited by in the applicants df and drop NaN values
    applic = applic.drop_duplicates('invited_by')
    # add an emptype column with talent
    applic["emp_type"] = "talent"
    # return only the invited by and emptype columns
    applic = applic[['invited_by','emp_type']]
    # rename the column for invitedby to staff
    applic.rename(columns={'invited_by':'staff'}, inplace=True)
    # appends the applic and academy tables to generate all staff
    staff = academy.append(applic)
    # runs the mispelling correction tool on the staff column
    # staff = mispell(staff,"staff")
    # returns the dataframe sorted first by emp type and then by name
    staff = staff.sort_values(["emp_type", "staff"], ascending=True)
    staff = staff.dropna()
    # add a unique Id
    staff.insert(0, 'staff_id', range(1, 1 + len(staff)))


    # return the dataframe
    return staff
