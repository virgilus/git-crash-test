import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())


print (f"average age : {dataset["age"].mean()}")

