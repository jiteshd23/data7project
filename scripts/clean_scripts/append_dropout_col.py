import numpy as np

class DropoutCol:
    def __init__(self, dataframe):
        self._df = dataframe

    def create_dropout_col(self):
        df = self._df
        df['dropout'] = 1
        for col in df.columns[:-1]:
            df['dropout'] = np.where(df[col] == 0, 0, df['dropout'])
        return df

