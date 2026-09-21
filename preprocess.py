import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())
<<<<<<< HEAD
# Virgile
print(df['age'].mean())
=======
#Added by Vicente
print("Average score:", df["score"].mean())
>>>>>>> main
=======
# Added by Rodrigo
print("Average score:", df["score"].mean())

#Added by Ebube
print("Average score:", df["score"].mean())
