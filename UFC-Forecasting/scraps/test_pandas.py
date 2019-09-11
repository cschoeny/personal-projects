import pandas as pd
import os

# First just try reading in the csv files.
dirname = os.path.abspath('')
filename = dirname + "/data/event_stats.csv"

df = pd.read_csv(filename)
df.head()
df = df.dropna()
df.head()
df.columns
df.Str = df.Str.astype(int)
df.head()

convert_dict = {'Str': int,
                'Td': int,
                'Sub': int,
                'Pass': int,
                'Round': int
               }

df = df.astype(convert_dict)
df.head()

# First just try reading in the csv files.
dirname = os.path.abspath('')
filename = dirname + "/data/fight_stats.csv"

df = pd.read_csv(filename)

df.head()

# Drop any nulls
df = df.dropna()
# Don't need some of the rows.
df = df.drop(['Sig. str. %', 'Total str.', 'Td %'], axis=1)
df.head()

# Need to right a function to only take the 1st number in Sig str & TD columns
def landed(num_of_num):
    num, _, _ = num_of_num.partition(' of')
    return int(num)

aa = landed('56 of 154')
type(aa)

df['Sig. str.'] = df['Sig. str.'].apply(lambda x: landed(x))
df['Td'] = df['Td'].apply(lambda x: landed(x))

df.info()
