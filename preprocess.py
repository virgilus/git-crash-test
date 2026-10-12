import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())

# Added by Dario
print("Average score:", df["score"].mean())
# Addes by Milan
print("Max score:", df["score"].max())