'''
2. Perform Exploratory Data Analysis for the dataset  salary_data. 
   The dataset can be downloaded from  https://www.kaggle.com/datasets
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Salary_Data.csv')
print("First 5 rows:\n", df.head())

print("\nInfo:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.histplot(df['Experience_Years'], kde=True)
plt.title('Experience Years Distribution')

plt.subplot(1, 3, 2)
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')

plt.subplot(1, 3, 3)
sns.histplot(df['Salary'], kde=True)
plt.title('Salary Distribution')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 4))
sns.countplot(x='Gender', data=df)
plt.title('Gender Count')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Gender', y='Salary', data=df)
plt.title('Salary by Gender')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Experience_Years', y='Salary', hue='Gender', data=df)
plt.title('Experience vs Salary')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='Salary', hue='Gender', data=df)
plt.title('Age vs Salary')
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()