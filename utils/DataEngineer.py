
from sklearn.preprocessing import label_binarize
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
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
        self.df = self.df.drop(columns_list, axis=1)


    def fill_none_data(self, flag, index):
        try:
            if flag in self.fill_flag_list:
                if flag == "ffill":
                    self.df[index] = self.df[index].fillna(method="ffill")
                elif flag == "drop":
                    self.df = self.df.dropna(axis=0, subset=[index], inplace=False)
                elif flag == "zero":
                    self.df[index] = self.df[index].fillna(0)
                elif flag == "bfill":
                    self.df[index] = self.df[index].fillna(method="bfill")
                elif flag == "mid":
                    imputer_mid = SimpleImputer(strategy="median")
                    self.df[index] =imputer_mid.fit_transform(self.df[index].values.reshape(-1, 1))
            else:
                raise ValueError
        except ValueError:
            print("you must input string in ['ffill', 'drop', 'zero', 'bfill','mid']")
