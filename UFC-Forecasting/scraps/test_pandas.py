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


# Now let's test how to properly merge them

#First read in the 2 pkl files
dirname = os.path.abspath('')
filename_event_pkl = dirname + "/data/event_stats.pkl"
filename_fight_pkl = dirname + "/data/fight_stats.pkl"

df_e = pd.read_pickle(filename_event_pkl)
df_f = pd.read_pickle(filename_fight_pkl)


# Will want to join on name, sig str, td
df_e.info()

df_f.info()

df = df_e.merge(df_f, how='inner', left_on=['Fighter', 'Str', 'Td', 'Pass', 'Sub'], right_on=['Fighter', 'Sig. str.', 'Td', 'Pass', 'Sub. att'])
df.info()
df.head()

# Not 100% clear how we merged 1763 and 1766 and got a dataframe with 1777.
# Apparently Francis Ngannou gained 4 fights??
df = df.drop_duplicates()
df.info()

# Okay so there are fights with identical shared stats. There aren't that many so it's going to be okay.
# Time to clean it up
# Can drop the following columns W/L, 'Sig. Str.', Sub. att
df = df.drop(['W/L', 'Sig. str.', 'Sub. att'], axis=1)
df.head()

# Now time to add the score
# Let's first make a round point column
def round_points(round, time):
    if round==1:
        return 90
    elif round==2:
        return 70:
    elif round==3 or round==5:
        if time=='5:00':
            return 40
        else:
            return 50
    elif round==4:
        return 50
    else:
        raise ValueError('Not valid round information')
