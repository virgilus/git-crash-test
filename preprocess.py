import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())
# Added by shadacas03-a11y
print("Average score:", df["score"].mean())