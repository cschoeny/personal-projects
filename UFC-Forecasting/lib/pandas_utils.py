import pandas as pd
import os


def create_pkl():
    return None


# Read in the csv
dirname = os.path.abspath('')
filename = dirname + "/data/UFC_stats.csv"
df = pd.read_csv(filename)

df = df.dropna()
df.info()
