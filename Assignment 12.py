import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

df = pd.read_csv("customer_churn.csv")

print(df.head())
print(df.info())
print(df.columns)

print(df.describe())
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Mode:\n", df.mode().iloc[0])
print("Variance:\n", df.var(numeric_only=True))
print("Standard Deviation:\n", df.std(numeric_only=True))
print("Minimum:\n", df.min(numeric_only=True))
print("Maximum:\n", df.max(numeric_only=True))
print("Percentiles:\n", df.quantile([0.25, 0.50, 0.75], numeric_only=True))

df.hist(figsize=(10, 8))
plt.show()

sns.boxplot(data=df.select_dtypes(include="number"))
plt.show()

num = df.select_dtypes(include="number")

plt.scatter(num.iloc[:, 0], num.iloc[:, 1])
plt.show()

corr = num.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

print(df.isnull().sum())

df = df.dropna()
print(df)

z = num.apply(zscore)
outliers = (abs(z) > 3)
print(df[outliers.any(axis=1)])

df = df[(abs(z) <= 3).all(axis=1)]

print(df.isnull().sum())
print(df)
print(df.describe())

df.to_csv("cleaned_customer_churn.csv", index=False)
