# Data set used 
# https://www.kaggle.com/datasets/shreyanshverma27/water-quality-testing?resource=download 


import pandas as pd
#import numpy as np
from matplotlib import pyplot as plt #for it to work in terminal for somereason
#from scipy import stats
import seaborn as sns
sns.set() #sets plotting style to default

Water_Quality=pd.read_csv("C:\\Users\\jonat\\Documents\\CODE lancashire\\Python CODE LANCS\\python homework\\Water Quality Testing.csv", sep=",")

print(Water_Quality.head())

#X = wine_df.drop(["quality", "Id"], axis=1) #dataset without Quality and ID
#Y = wine_df["quality"]#data set with just Quality
#print(Y)

X = Water_Quality.drop(["Sample ID"], axis=1)
print(X.head())
Corr_Matrix = X.corr() # creates a correlation matrix to visualise which values are correlated

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10,6))
sns.heatmap(Corr_Matrix, annot=True,cmap="coolwarm",vmin=-1,vmax=1)
plt.show()
Corr_Matrix = Corr_Matrix.abs()

Corr_Matrix["SUM"]= Corr_Matrix.sum(axis=1)-1
print(Corr_Matrix)



Y = X["Dissolved Oxygen (mg/L)"]
X = X.drop(["Dissolved Oxygen (mg/L)"], axis=1)

shapiro_table = pd.DataFrame(columns=["Variable", "Statistic", "p_value", "Normal", "Correlation", "Correlation significance"])

#Needs these to work in terminal
from scipy.stats import shapiro
from scipy.stats import spearmanr
from scipy.stats import pearsonr

print("          ")
print("          ")
N=0
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(20, 5)) 
for column in Water_Quality:
    if column != "Sample ID":
        axes[N].hist(Water_Quality[column])
        axes[N].set_title(column)
        N+=1

for column in X.columns:
    column_var = X[column]
    column_ind = Y

    statistic, p_value = shapiro(column_var)
    shap_statistic = statistic
    shap_p_value = p_value
    #print(f"{column} Statistic = {statistic} p_value = {p_value}")
    if p_value <= 0.05:
        normality= "True"
        statistic, p_value = spearmanr(column_ind, column_var)
        cor_p_value=p_value
        cor_statistic = statistic
    else:
        normality="False"
        statistic, p_value = pearsonr(column_ind, column_var)
        cor_p_value=p_value
        cor_statistic=statistic
    shapiro_table = shapiro_table._append({"Variable" : column, "Statistic" : shap_statistic, "p_value" : shap_p_value, "Normal" : normality, "Correlation" : cor_statistic, "Correlation significance" : cor_p_value}, ignore_index=True)
    
print(shapiro_table)
print("          ")
print("          ")

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 10))
N= 0
for column in Water_Quality:
    if column != "Sample ID" and column != "Dissolved Oxygen (mg/L)":
        sns.regplot(x=column, y="Dissolved Oxygen (mg/L)", data=Water_Quality, ax=axes[0,N])
        #axes[0,N].set_title(f"{column} vs Dissolved Oxygen")
        N+=1

#print(Water_Quality.keys())

N=0
for column in Water_Quality:
    if column != "Sample ID" and column != "Conductivity (µS/cm)":
        sns.regplot(x=column, y="Conductivity (µS/cm)", data=Water_Quality, ax=axes[1,N])
        #axes[1,N].set_title(f"{column} vs Conductivity (µS/cm)")
        N+=1
plt.show()






