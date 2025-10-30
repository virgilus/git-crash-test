import pandas as pd

df = pd.read_csv("../data/dataset.csv")
while True:
    print(df.describe())
print(df.describe())


print (f"average age : {dataset["age"].mean()}")
# Added by rim:
print("Average score:", df["score"].mean())
