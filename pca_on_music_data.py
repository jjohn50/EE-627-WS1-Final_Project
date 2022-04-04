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

df2["Predictor"]= (df["Predictor"]+df["Predictor1"])/2
print(df2)
 
df2.to_csv("output14.csv",index=None)