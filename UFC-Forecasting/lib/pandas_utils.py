import pandas as pd
import os


def read_clean_save_event_stats():
    dirname = os.path.abspath('')
    filename = dirname + "/data/event_stats.csv"

    df = pd.read_csv(filename)
    df = df.dropna()
    df = df[df['W/L'] == 'win']
    df = df[df['Method'] != 'DQ']

    convert_dict = {'Str': int,
                    'Td': int,
                    'Sub': int,
                    'Pass': int,
                    'Round': int
                    }

    df = df.astype(convert_dict)

    filename_pkl = dirname + "/data/event_stats.pkl"
    df.to_pickle(filename_pkl)


def read_clean_save_fight_stats():
    dirname = os.path.abspath('')
    filename = dirname + "/data/fight_stats.csv"

    df = pd.read_csv(filename)
    df = df.dropna()
    df = df.drop(['Sig. str. %', 'Total str.', 'Td %'], axis=1)

    def landed(num_of_num):
        num, _, _ = num_of_num.partition(' of')
        return int(num)

    df['Sig. str.'] = df['Sig. str.'].apply(lambda x: landed(x))
    df['Td'] = df['Td'].apply(lambda x: landed(x))

    filename_pkl = dirname + "/data/fight_stats.pkl"
    df.to_pickle(filename_pkl)


def merge_two_stat_sources():
    pass
