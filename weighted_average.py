import numpy
import pandas as pd 
df = pd.read_csv("output2_copy.csv")
df["UserID"] = df["UserID"].astype(str)
df["TrackID"] = df["TrackID"].astype(str)
df2 = pd.DataFrame(columns = ['TrackID',"Predictor"])
# print(df2)  
# print(df["UserID"])
# print(df["TrackID"])
df2["TrackID"]=df["UserID"] + "_" + df["TrackID"]

df["Predictor"] = df["Predictor"].astype(int)
# print(df["Predictor1"])
df["Predictor1"] = df["Predictor1"].astype(int)
weight1 = 0.95
weight2 = 0.15 

df2["Predictor"]= (weight1*df["Predictor"]+weight2*df["Predictor1"])/2
print(df2)
 
df2.to_csv("0.95_0.15_output14.csv",index=None)    

