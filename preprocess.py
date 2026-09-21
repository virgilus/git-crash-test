import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())

print("Adubea Average score:", df["score"].mean())