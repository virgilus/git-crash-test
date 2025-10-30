import pandas as pd

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

<<<<<<< HEAD

=======
# Added by Giovanni
print("Average score:", df["score"].mean())
>>>>>>> main

print("min score:", df["score"].min())