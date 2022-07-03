import pandas as pd
import statistics as st
from sklearn.datasets import load_boston


def task():
    read_file = pd.read_excel("Monster_Hunt.xlsx")  # import the spreadsheet in your project and paste it's name here
    read_file.to_csv("SPOILER_Monster_Hunt.csv",
                     index=None,
                     header=True)
    # read csv file and convert
    # into a dataframe object
    df = pd.DataFrame(pd.read_csv("SPOILER_Monster_Hunt.csv"))
    df.columns = ["S/No", "Member_Name", "L1", "L2", "L3", "L4", "L5"]
    #some modifications below
    df = df.drop(index=0)
    df = df.drop(columns='S/No')
    df = df.fillna(0)

    #Adjusting points with monster levels

    df['L1'] = df['L1'].astype(int)
    df['L1'] = df['L1'] * 50
    df['L2'] = df['L2'].astype(int)
    df['L2'] = df['L2'] * 150
    df['L3'] = df['L3'].astype(int)
    df['L3'] = df['L3'] * 300
    df['L4'] = df['L4'].astype(int)
    df['L4'] = df['L4'] * 1000
    df['L5'] = df['L5'].astype(int)
    df['L5'] = df['L5'] * 2000
    df['Total_points'] = df['L1'] + df['L2'] + df['L3'] + df['L4'] + df['L5']
    df['Total_points'] = df['Total_points'].astype(int)
    print(df)
    print("\t\t THE WINNER IS:")
    print(df.loc[df['Total_points'] == df['Total_points'].max()])


task()