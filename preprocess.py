import pandas as pd

df = pd.read_csv("../data/dataset.csv")
df.head()
print(df.describe())
#  add one extra line of code
print("Average score:", df["score"].mean())
