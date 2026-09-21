import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.describe())

#Added by Adubea
print("Adubea Average score:", df["score"].mean())

# Virgile
print(df['age'].mean())

#Added by Vicente
print("Average score:", df["score"].mean())

=======

# Added by Rodrigo
print("Average score:", df["score"].mean())

#Added by Ebube
print("Average score:", df["score"].mean())
