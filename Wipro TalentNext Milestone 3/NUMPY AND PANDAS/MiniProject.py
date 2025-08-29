''' 
Use Case:Perform   the   Outlier   detection   for   the   given dataset   i.e.datasetExample
Dataset :    datasetExample.csv

Perform the following task 
•Load the data in the DataFrame.
•Detection of Outliers.

'''

import pandas as pd

df = pd.read_csv('datasetExample.csv')
print(df)

numeric_df = df.select_dtypes(include='number')
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

outliers = (numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))
print("\nOutliers detected :")
print(outliers)

