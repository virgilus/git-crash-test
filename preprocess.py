import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())

# Added by Dario
print("Average score:", df["score"].mean())

#Added by Léa
print("Min score:", df["score"].min())