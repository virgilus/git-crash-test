import pandas as pd

df = pd.read_csv("../data/dataset.csv")
while True:
    print(df.describe())