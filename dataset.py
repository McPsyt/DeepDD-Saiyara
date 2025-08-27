import pandas as pd
import os
from pandas import read_parquet

path = "/data/benlab/DeepDD/GENEActiv_Data/Data/DEEP DD-GENEActiv Data/"

#Parquet is efficient memory storage

def open_csv(csv_path):
    df = pd.read_csv(csv_path, skiprows=100)
    df.to_parquet("./parquet/"+csv_path.strip(".csv")+".parquet")

def get_seq(label, data_path, name):
    df = pd.read_parquet(data_path)
    df_new = df[df["date"] == label]
    df_new.to_parquet(name, index=False)

