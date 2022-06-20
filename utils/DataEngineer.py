
from sklearn.preprocessing import label_binarize
import pandas as pd
from sklearn.impute import SimpleImputer

class DataEngineer():

    def __init__(self, df):
        self.df = df
        self.fill_flag_list = ["ffill", "drop", "zero", "bfill", "mid"]

    def get_dataframe(self):
        return self.df

    def count_none_data(self):
        columns_count = self.df[self.df.columns].isna().sum()
        print(columns_count)

    def drop_columns(self, columns_list):
        self.df.drop(columns_list)

    def fill_none_data(self, flag, index):
        try:
            if flag in self.fill_flag_list:
                if flag == "ffill":
                    self.df[index] = self.df[index].fillna(method="ffill")
                elif flag == "drop":
                    self.df[index] = self.df[index].dropna(axis=0)
                elif flag == "zero":
                    self.df[index] = self.df[index].fillna(0)
                elif flag == "bfill":
                    self.df[index] = self.df[index].fillna(method="bfill")
                elif flag == "mid":
                    imputer_mid = SimpleImputer(strategy='median')
                    imputer_mid.fit(self.df[index].values)
                    numeric_data = imputer_mid.transform(self.df[index].values)
                    self.df[index].values = numeric_data
            else:
                raise ValueError
        except ValueError:
            print("you must input string in ['ffill', 'drop', 'zero', 'bfill','mid']")
