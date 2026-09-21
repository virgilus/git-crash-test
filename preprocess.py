import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())
# Added by Ihab-Abumustafa
print("Average score:", df["score"].mean())