
import pandas as pd


if __name__ == "__main__":
    train_data_path  = "./dataset/train.csv"
    test_data_path = "./dataset/test.csv"
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    print(train_df)

