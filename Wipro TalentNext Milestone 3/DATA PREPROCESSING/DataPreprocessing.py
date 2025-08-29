'''
            1.  USING SK-LEARN
Perform Data Preprocessing on melb_data.csv dataset with statistical perspective.

The dataset can be downloaded from
https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download

'''

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv('melb_data.csv')

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)])

df_processed = preprocessor.fit_transform(df)

print("Processed data shape:", df_processed.shape)

'''
            2.  USING PANDAS
Perform Data Preprocessing on melb_data.csv dataset with statistical perspective.

The dataset can be downloaded from
https://www.kaggle.com/datasets/gunjanpathak/melb-data?resource=download  
        
'''
import pandas as pd

df = pd.read_csv('melb_data.csv')

# Drop columns that are not useful for modeling (example: Address, SellerG, Date)
columns_to_drop = ['Address', 'SellerG', 'Date']
df = df.drop(columns=columns_to_drop, errors='ignore')

# Drop duplicate rows
df = df.drop_duplicates()

# Handle missing values
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

print("Processed data shape:", df_encoded.shape)
print("First 5 rows:\n", df_encoded.head())