import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

#added by Clémentine
print("Average score:", df["score"].mean()) 
# Added by Giovanni
print("Average score:", df["score"].mean())
while True:
    print(df.describe())
print(df.describe())


print (f"average age : {dataset["age"].mean()}")

