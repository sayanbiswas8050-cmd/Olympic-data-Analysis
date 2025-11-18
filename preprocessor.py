
import pandas as pd


def preprocess(df,region_df):
    
    # filtering for summer Olympic
    df =df[df["Season"] == "Summer"]
    # merge with region_df
    df = df.merge(region_df,on="NOC",how= "left")
    # drop the duplicates
    df .drop_duplicates(inplace=True)
    # concate different different medals(gold,silver,bronze) in mean df 
    df=pd.concat([df,pd.get_dummies(df["Medal"])],axis=1)
    return df

