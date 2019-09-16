# Convert to jupyter notebook later (currently on plane and can't do it cause don't have it installed)
import pandas as pd
import os

# Read in the combined stats file
dirname = os.path.abspath('')
filename_pkl = dirname + "/data/combined_stats.pkl"
df = pd.read_pickle(filename_pkl)

df.head()
