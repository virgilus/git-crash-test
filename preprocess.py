import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

# Added by Gouaref
print("Average score:", df["score"].mean())

# Added by Comlan
print("Average score:", df["score"].mean())
