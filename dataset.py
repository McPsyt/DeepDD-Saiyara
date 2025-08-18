import pandas as pd
import os


from pandas import read_parquet

path = "/data/benlab/DeepDD/GENEActiv_Data/Data/DEEP DD-GENEActiv Data/"

#Parquet is efficient memory storage

def open_csv(csv_path):
    df = pd.read_csv(path + csv_path, skiprows=100)
    df.to_parquet("./parquet/"+csv_path.strip(".csv")+".parquet")



if __name__ == "__main__":
   #df = pd.read_csv("DD102024016_left wrist_107722_2025-08-04 16-21-07.csv", skiprows=100)
   #df.to_parquet("./parquet/DD_10_2024_016/Month 3/DD102024016_left wrist_107722_2025-08-04 16-21-07.parquet")
    df_month_2 = read_parquet("parquet/DD_10_2024_016/Month 2/DD102024016_left wrist_100889_2025-07-09 13-41-33.parquet")
    print(df_month_2)