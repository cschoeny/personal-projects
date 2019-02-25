# %% Reading in and formatting individual stats
import pandas as pd
# import numpy as np


def main():
    df_bog = pd.read_csv('../raw_data/raw_2019/bogey_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'TOTAL BOGEYS', 'ROUNDS PLAYED'])
    df_bog = df_bog.rename(index=str, columns={'TOTAL BOGEYS': 'B', 'ROUNDS PLAYED': 'Rounds'})

    df_db = pd.read_csv('../raw_data/raw_2019/doublebogey_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'TOTAL BOGEYS AND WORSE'])
    df_db = df_db.rename(index=str, columns={'TOTAL BOGEYS AND WORSE': 'DBoW'})

    df_bir3 = pd.read_csv('../raw_data/raw_2019/par3_bird_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'PAR 3 BIRDIES OR BETTER', 'PAR 3 HOLES'])
    df_bir3 = df_bir3.rename(index=str, columns={'PAR 3 BIRDIES OR BETTER': 'P3b', 'PAR 3 HOLES': 'P3H'})

    df_eag4 = pd.read_csv('../raw_data/raw_2019/par4_eag_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'TOTAL'])
    df_eag4 = df_eag4.rename(index=str, columns={'TOTAL': 'P4e'})

    df_bir4 = pd.read_csv('../raw_data/raw_2019/par4_bird_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'PAR 4 BIRDIES OR BETTER', 'PAR 4 HOLES'])
    if df_bir4['PAR 4 HOLES'].dtype == 'O':  # need this if the number includes commas and quotes
        df_bir4['PAR 4 HOLES'] = df_bir4['PAR 4 HOLES'].str.replace(',', '').astype(float)
    df_bir4 = df_bir4.rename(index=str, columns={'PAR 4 BIRDIES OR BETTER': 'P4be', 'PAR 4 HOLES': 'P4H'})

    df_eag5 = pd.read_csv('../raw_data/raw_2019/par5_eag_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'TOTAL'])
    df_eag5 = df_eag5.rename(index=str, columns={'TOTAL': 'P5e'})

    df_bir5 = pd.read_csv('../raw_data/raw_2019/par5_bird_2019.csv', header=0, index_col='PLAYER NAME', usecols=['PLAYER NAME', 'PAR 5 BIRDIES OR BETTER', 'PAR 5 HOLES'])
    df_bir5 = df_bir5.rename(index=str, columns={'PAR 5 BIRDIES OR BETTER': 'P5be', 'PAR 5 HOLES': 'P5H'})

    # %% Joining to create overall dataframe
    # Now I join them all
    df = df_bog.join(df_db).join(df_bir3).join(df_eag4).join(df_bir4).join(df_eag5).join(df_bir5)
    df = df.fillna(0)  # this is just for eagle

    # Now subtract eagles from birdies or better to get just birdies
    df['P4b'] = df['P4be'].subtract(df['P4e'])
    df = df.drop('P4be', axis=1)

    df['P5b'] = df['P5be'].subtract(df['P5e'])
    df = df.drop('P5be', axis=1)

    # Now subtract bogeys from bogeys or worse to get double bogeys (or worse)
    df['DB'] = df['DBoW'].subtract(df['B'])
    df = df.drop('DBoW', axis=1)

    # Regression to means based on number of rounds.
    # df['P3b'] = df['P3b'] + (np.sum(df['P3b'])/np.sum(df['P3H'])) * df['P3H'].mean() / 6
    # df['P3H'] = df['P3H'] + df['P3H'].mean() / 6
    # df['P4b'] = df['P4b'] + (np.sum(df['P4b'])/np.sum(df['P4H'])) * df['P4H'].mean() / 6
    # df['P4e'] = df['P4e'] + (np.sum(df['P4e'])/np.sum(df['P4H'])) * df['P4H'].mean() / 6
    # df['P4H'] = df['P4H'] + df['P4H'].mean() / 6
    # df['P5b'] = df['P5b'] + (np.sum(df['P5b'])/np.sum(df['P5H'])) * df['P5H'].mean() / 6
    # df['P5e'] = df['P5e'] + (np.sum(df['P5e'])/np.sum(df['P5H'])) * df['P5H'].mean() / 6
    # df['P5H'] = df['P5H'] + df['P5H'].mean() / 6
    # df['B'] = df['B'] + (np.sum(df['B'])/np.sum(df['Rounds'])) * df['Rounds'].mean() / 6
    # df['DB'] = df['DB'] + (np.sum(df['DB'])/np.sum(df['Rounds'])) * df['Rounds'].mean() / 6
    # df['Rounds'] = df['Rounds'] + df['Rounds'].mean() / 6

    # Saving dataframe
    df.to_pickle('../stats/stats_2019.pkl')


if __name__ == '__main__':
    main()
