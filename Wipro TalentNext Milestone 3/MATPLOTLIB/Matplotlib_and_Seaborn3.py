'''
3. Perform Exploratory Data Analysis for the dataset  Social Network Ads. 
   The dataset can be downloaded from  https://www.kaggle.com/datasets
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Social_Network_Ads.csv')
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
sns.histplot(df['EstimatedSalary'], kde=True)
plt.title('Estimated Salary Distribution')

plt.subplot(1, 3, 3)
sns.countplot(x='Purchased', data=df)
plt.title('Purchased Distribution')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Purchased', y='Age', data=df)
plt.title('Age by Purchased')
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x='Purchased', y='EstimatedSalary', data=df)
plt.title('Estimated Salary by Purchased')
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='EstimatedSalary', hue='Purchased', data=df)
plt.title('Age vs Estimated Salary by Purchased')
plt.show()

plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
