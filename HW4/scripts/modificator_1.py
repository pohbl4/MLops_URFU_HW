# DON'T FORGET INSTALL DEPENDENCIES
# pip install numpy pandas
import numpy as np
import pandas as pd


train_path, test_path = "../titanic-dataset/train.csv", "../titanic-dataset/test.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)


# FILL NULL ROWS FOR AGE COLUMN
def fill_mean_value_for_age_column(df):
    if df['Age'].isna().sum() > 0:
        df['Age'] = df['Age'].fillna(int(np.mean(df['Age'])))


# CHECK COLUMN
def check_column_on_empty_rows(df, df_name):
    if df['Age'].isna().sum() == 0:
        print(f"Age column is ready for use: {df_name}")
    else:
        print(f"Age column is not ready for use: {df_name}")


fill_mean_value_for_age_column(train_df)
fill_mean_value_for_age_column(test_df)

check_column_on_empty_rows(train_df, "train")
check_column_on_empty_rows(test_df, "test")
