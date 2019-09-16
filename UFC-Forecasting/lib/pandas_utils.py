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


def merge_two_stat_sources_and_score():
    dirname = os.path.abspath('')
    filename_event_pkl = dirname + "/data/event_stats.pkl"
    filename_fight_pkl = dirname + "/data/fight_stats.pkl"

    df_e = pd.read_pickle(filename_event_pkl)
    df_f = pd.read_pickle(filename_fight_pkl)

    df = df_e.merge(df_f, how='inner', left_on=['Fighter', 'Str', 'Td', 'Pass', 'Sub'], right_on=['Fighter', 'Sig. str.', 'Td', 'Pass', 'Sub. att'])
    df = df.drop_duplicates()

    # NEED TO GET THE REAL NUMBERS FROM DK HERE
    def round_points(round, time):
        if round == 1:
            return 90
        elif round == 2:
            return 70
        elif round == 3 or round == 5:
            if time == '5:00':
                return 30
            elif round == 3:
                return 45
            else:
                return 40
        elif round == 4:
            return 40
        else:
            raise ValueError('Not valid round information')

    # NEED TO GET THE REAL NUMBERS FROM DK HERE
    df['Round_Points'] = df.apply(lambda x: round_points(x['Round'], x['Time']), axis=1)
    df['DK_Points'] = 0.5 * df['Str'] + 5 * df['Td'] + 3 * df['Pass'] + 10 * df['KD'] + 5 * df['Rev.'] + df['Round_Points']

    df = df.drop(['W/L', 'Sig. str.', 'Sub. att', 'Sub', 'Round_Points'], axis=1)

    def combine_dec(method):
        if 'DEC' in method:
            return 'DEC'
        else:
            return method

    df['Method'] = df.apply(lambda x: combine_dec(x['Method']), axis=1)

    def round_cat(Round, Method):
        if Method == 'DEC':
            return str(Round) + ' ' + Method
        else:
            return str(Round)

    df['Round_Cat'] = df.apply(lambda x: round_cat(x['Round'], x['Method']), axis=1)

    filename_pkl = dirname + "/data/combined_stats.pkl"
    df.to_pickle(filename_pkl)
