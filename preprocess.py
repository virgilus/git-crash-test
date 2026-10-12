import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())

# Added by Dario
print("Average score:", df["score"].mean())

# Added by Daignon-Max
print("Max score:", df["score"].max())