import pandas as pd
import os


from pandas import read_parquet

path = "/data/benlab/DeepDD/GENEActiv_Data/Data/DEEP DD-GENEActiv Data/"

#Parquet is efficient memory storage

def open_csv(csv_path):
    df = pd.read_csv(csv_path, skiprows=100)
    df.to_parquet("./parquet/"+csv_path.strip(".csv")+".parquet")



if __name__ == "__main__":
   open_csv("DD072024007_left wrist_101696_2024-10-22 15-22-36.csv")