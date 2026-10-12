import pandas as pd

df = pd.read_csv("dataset.csv")
<<<<<<< HEAD
print(df.describe()) 
=======
print(df.describe())

# Added by Dario
print("Average score:", df["score"].mean())
>>>>>>> 86908e7ad53627cff37a0694f5fdc9793aa7e9e4
