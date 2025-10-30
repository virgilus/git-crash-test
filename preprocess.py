import pandas as pd

df = pd.read_csv("../data/dataset.csv")
# Added by YourName
print("Average score:", df["score"].mean())print(df.describe())


