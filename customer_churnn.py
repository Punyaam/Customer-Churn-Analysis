"""
Customer Churn Analysis
Author: Punya A M
Description:
This project analyzes telecom customer data to identify key factors
that contribute to customer churn using exploratory data analysis.
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries loaded successfully")


df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset loaded successfully")
print(df.shape)        # rows, columns
print(df.columns)      # column names


# ================== DATA CLEANING ==================

# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing TotalCharges with median
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())

# Convert Churn to numeric (target variable)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

print("\nData cleaning completed successfully")



# ================== EDA ==================

churn_rate = df['Churn'].mean()
print(f"\nOverall Churn Rate: {churn_rate:.2f}")


print("\nChurn Rate by Contract Type:")
print(df.groupby('Contract')['Churn'].mean())


print("\nAverage Tenure by Churn:")
print(df.groupby('Churn')['tenure'].mean())


print("\nAverage Monthly Charges by Churn:")
print(df.groupby('Churn')['MonthlyCharges'].mean())



sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")
plt.show()


sns.barplot(x='Contract', y='Churn', data=df)
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate")
plt.show()


sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.show()

# ================== KEY INSIGHTS ==================
# 1. Month-to-month contract customers have the highest churn rate.
# 2. Customers with higher monthly charges are more likely to churn.
# 3. Long-tenure customers show greater loyalty and lower churn.




