import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())
#Added by Vicente
print("Average score:", df["score"].mean())