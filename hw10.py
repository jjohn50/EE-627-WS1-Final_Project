import pandas as pd 
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
  
df = pd.read_csv('ensemble_learning_format2.csv')

# names = df.columns
# names=names[2:]  

names = ['Sub_1_87733','Sub_2_77585', 'Sub_3_84310','Sub_4_87863','Sub_5_87455','Sub_6_87866','Sub_7_87869','Sub_8_87871','Sub_9_87873','Sub_10_87871','Sub_11_88247','Sub_12_87205','Sub_13_86602','Sub_14_89658','Sub_15_61561','Sub_16_89210','Sub_17_49474','Sub_18_50804','Sub_19_84507','Sub_20_84507','Sub_21_82108','Sub_22_82108','Sub_23_84398']
# print(df)  
# print(df[names].values)
S = df[names].values
# print(S.shape)
# print(type(S))
score = [0.87733,0.77585,0.8431,0.87863,0.87455,0.87866,0.87869,0.87871,0.87873,0.87871,0.88247,0.87205,0.86602,0.89658,0.61561,0.8921,0.49474,0.50804,0.84507,0.84507,0.82108,0.82108,0.84398]

length = len(df)
St_x = []

St_x = [length * (2*J-1) for J in score]

St_s = np.dot(S.T, S).astype('float') + np.eye(S.shape[1]) * (10 ** -6)
   
St_s_inv = np.linalg.inv(St_s)
# print(St_s_inv.shape)
# print(St_s_inv)

a_LS = np.dot(St_s_inv,St_x)
# print(a_LS)    

S_ensemble = np.dot(S,a_LS)
# print(S_ensemble)  
S_ensemble_len = len(S_ensemble)
print(S_ensemble_len)

final_predictions = np.zeros(S_ensemble_len)

for index in range(S_ensemble_len // 6):    # floor division
    # Threshold is the third element in the sorted array
    user_score_threshold = np.sort(S_ensemble[index * 6 : index * 6 + 6])[2]    # sort the 6 values for each user and grab the third element
    for index_user in range(6):
        if S_ensemble[index * 6 + index_user] > user_score_threshold:
            final_predictions[index * 6 + index_user] = 1

final_predictions_df = pd.DataFrame(df.iloc[:,1]) 
final_predictions_df['Predictor'] = np.array(final_predictions, dtype=int)
print(final_predictions_df)
final_predictions_df.to_csv('Ensemble_Predictions_Test1.csv', index=False)


















































