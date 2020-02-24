class MainClean:
    def __init__(self, table):
        self.table = table

        # takes in a unclean table and converts nan to 0 and adds column at the end.
        # column is those who completed the course.
        # this should have return a clean table.

    def performance_clean(self, df):
        fail = []
        for i in df[df.columns[-1]]:
            if i < 1:
                fail.append('False')
            else:
                fail.append('True')
        df['Completed'] = fail
