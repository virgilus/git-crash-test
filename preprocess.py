import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())

# Added by Dario
print("Averagescore:", df["score"].mean())

#Added by Théo
print('Average score:', df['score'].mean())
