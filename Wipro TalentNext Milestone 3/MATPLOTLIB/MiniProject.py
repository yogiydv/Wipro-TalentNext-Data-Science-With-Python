'''
Use Case  :   Diabetes Prediction 
Perform Exploratory Data Analysis for the Diabetes Dataset.

Dataset :  Diabetes.csv
The dataset can be downloaded from  https://www.kaggle.com/datasets

Perform the following tasks

1.Load the data in the DataFrame.
2.Data Pre-processing.
3.Handle the Categorical Data.
4.Perform Uni-variate Analysis. 
5.Perform Bi-variate Analysis.

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')
print("First 5 rows:\n", df.head())

cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)
df[cols_with_zero] = df[cols_with_zero].fillna(df[cols_with_zero].median())

print("\nUnique values in Outcome:", df['Outcome'].unique())

plt.figure(figsize=(12, 8))
for i, col in enumerate(df.columns[:-1]):
    plt.subplot(3, 3, i+1)
    sns.histplot(df[col], kde=True)
    plt.title(col)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='Outcome', data=df)
plt.title('Outcome Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title('Glucose vs Outcome')
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
