import numpy as np 
import pandas as pd

df = pd.read_csv("82_features.csv")
df["UserID"] = df["UserID"].astype(str)
df["TrackId"] = df["TrackId"].astype(str)
df["AlbumId"] = df["AlbumId"].astype(float)
df["Track"] = df["Track"].astype(float)
df["Genre1"] = df["Genre1"].astype(float)
df["Genre2"] = df["Genre2"].astype(float)
df["Genre3"] = df["Genre3"].astype(float)
df["Genre4"] = df["Genre4"].astype(float)
df["Genre5"] = df["Genre5"].astype(float)  
df["Genre6"] = df["Genre6"].astype(float)

df2 = pd.DataFrame(columns = ['TrackId','Predictor'])
# print(df2)  
# print(df["UserID"])
# print(df["TrackId"])  
df2["TrackId"]=df["UserID"] + "_" + df["TrackId"]   

# print(df["Predictor1"])
df2["Predictor"]= (df["AlbumId"]+df["ArtistId"]+df["Track"]+df["Genre1"]+df["Genre2"]+df["Genre3"]+df["Genre4"]+df["Genre5"]+df["Genre6"])/9

# use if statements to determine which items have values 
# from there we can make better prediction for weights and so on 

print(df2)   

df2.to_csv("8features_final_results_as_id_predictor_values.csv",index=None)    