import pandas as pd
import numpy as np

df = pd.read_csv("../data/dataset.csv")
print(df.describe())

np.mean(df)
