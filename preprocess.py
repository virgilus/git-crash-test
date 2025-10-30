import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

# Added by Giovanni
print("Average score:", df["score"].mean())
while True:
    print(df.describe())
print(df.describe())


print (f"average age : {dataset["age"].mean()}")

