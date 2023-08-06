
import pandas as pd
import seaborn as sns

def  da():
    df =sns.load_dataset("titanic")


    df.drop(0,axis=0,inplace=True)
    return print(df)


da()
