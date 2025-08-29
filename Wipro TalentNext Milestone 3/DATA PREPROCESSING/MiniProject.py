'''
Use-Case: House Price Prediction.

Dataset: melb_data.csv
The dataset can be downloaded melb data.csv | Kaggle

Perform the following tasks:
1. Load the data in dataframe (Pandas).
2. Handle inappropriate data.
3. Handle the missing data.
4. Handle the categorical data.
'''

import pandas as pd

df = pd.read_csv('melb_data.csv')

columns_to_drop = ['Address', 'SellerG', 'Date']  # Adjust as needed
df = df.drop(columns=columns_to_drop, errors='ignore')
df = df.drop_duplicates()

df = df.dropna(subset=['Price'])
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

df = pd.get_dummies(df, drop_first=True)

print(df.head())


