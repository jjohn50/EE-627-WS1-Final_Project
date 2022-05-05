import numpy as np 
import pandas as pd 


file = open("trainIdx2_matrix.txt")

df = pd.read_csv("trainIdx2_matrix.txt", sep="|",header=["userID","itemID","rating"])
print(df)

# df.to_csv("trainIdx2_matrix_correct.csv",header=False) 