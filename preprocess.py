import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

#added by Clémentine
print("Average score:", df["score"].mean()) 