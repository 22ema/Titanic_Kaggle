
from sklearn.preprocessing import label_binarize
import pandas as pd

class DataEngineer():

    def __init__(self, df):
        self.df = df
        self.fill_flag_list = ["ffill", "drop"]

    def found_none_data(self, flag):
        try :
            if flag in self.fill_flag_list:
                if flag == "ffill":
                    self. df = self.df.fillna(method="ffill")
                elif flag == "drop":
                    self. df = self.df.fillna(method="ffill") ## 여기서 부터 수정
        except:
            print("you must input string in ['ffill', 'drop']")
