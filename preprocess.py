import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())
# Virgile
print(df['age'].mean())