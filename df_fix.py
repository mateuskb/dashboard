import pandas as pd
import numpy as np

df = pd.read_csv("data/train.csv")

df.drop('PassengerId', axis=1, inplace=True)
df.drop('Name', axis=1, inplace=True)
df.drop('Cabin', axis=1, inplace=True)

df.dropna(subset=['Age'], inplace=True)

df.to_csv("data/titanic.csv")
print(df.isnull().values.ravel().sum())