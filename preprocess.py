import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

# Average score
average_score = df['score'].mean()
print("Average score:", average_score)
