
import pandas as pd
from utils.DataEngineer import DataEngineer

if __name__ == "__main__":
    train_data_path = "./dataset/train.csv"
    test_data_path = "./dataset/test.csv"
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    DE = DataEngineer(train_df)
    DE.count_none_data()
    DE.drop_columns(['Cabin'])
    DE.fill_none_data("mid", 'Age')
    DE.fill_none_data("drop", 'Embarked')
    DE.count_none_data()
    train_df = DE.get_dataframe()

    print(train_df[["Age", "Embarked"]].head())
