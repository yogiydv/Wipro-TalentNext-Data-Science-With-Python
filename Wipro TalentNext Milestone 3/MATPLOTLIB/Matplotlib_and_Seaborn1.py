'''
1. Perform Exploratory Data Analysis for the dataset Mall_Customers. 
   The dataset can be downloaded from  https://www.kaggle.com/datasets
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mall_Customers.csv')
print("First 5 rows:\n", df.head())

print("\nInfo:")
print(df.info())
print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:\n", df.isnull().sum())

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')

plt.subplot(1, 3, 2)
sns.histplot(df['Annual Income (k$)'], kde=True)
plt.title('Annual Income Distribution')

plt.subplot(1, 3, 3)
sns.histplot(df['Spending Score (1-100)'], kde=True)
plt.title('Spending Score Distribution')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 4))
sns.countplot(x='Genre', data=df)
plt.title('Gender Count')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Genre', y='Spending Score (1-100)', data=df)
plt.title('Spending Score by Gender')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Genre', data=df)
plt.title('Income vs Spending Score')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Genre', data=df)
plt.title('Age vs Spending Score')
plt.show()

