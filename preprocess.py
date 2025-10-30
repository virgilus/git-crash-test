import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

# Average score
average_score = df['score'].mean()
print("Average score:", average_score)
#added by Clémentine
print("Average score:", df["score"].mean()) 
while True:
    print(df.describe())
print(df.describe())


print (f"average age : {dataset["age"].mean()}")

