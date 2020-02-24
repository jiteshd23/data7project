import numpy as np


class DropoutCol:
    def __init__(self, dataframe):
        self._df = dataframe


    def fill_nanvalues(self):
        df = self.df.fillna(value=0)
        return df


