import pandas as pd
import numpy as np
import time


def main():
    # Read in the raw stats for each year
    df_2017 = pd.read_pickle('../stats/stats_2017.pkl')
    df_2018 = pd.read_pickle('../stats/stats_2018.pkl')
    df_2019 = pd.read_pickle('../stats/stats_2019.pkl')

    # Regress to the mean as a function of extremes and low holes/rounds
    df_2017['P3b'] = df_2017['P3b'] + (np.sum(df_2017['P3b']) / np.sum(df_2017['P3H'])) * df_2017['P3H'].mean() / 8
    df_2017['P3H'] = df_2017['P3H'] + df_2017['P3H'].mean() / 8
    df_2017['P4b'] = df_2017['P4b'] + (np.sum(df_2017['P4b']) / np.sum(df_2017['P4H'])) * df_2017['P4H'].mean() / 8
    df_2017['P4e'] = df_2017['P4e'] + (np.sum(df_2017['P4e']) / np.sum(df_2017['P4H'])) * df_2017['P4H'].mean() / 8
    df_2017['P4H'] = df_2017['P4H'] + df_2017['P4H'].mean() / 8
    df_2017['P5b'] = df_2017['P5b'] + (np.sum(df_2017['P5b']) / np.sum(df_2017['P5H'])) * df_2017['P5H'].mean() / 8
    df_2017['P5e'] = df_2017['P5e'] + (np.sum(df_2017['P5e']) / np.sum(df_2017['P5H'])) * df_2017['P5H'].mean() / 8
    df_2017['P5H'] = df_2017['P5H'] + df_2017['P5H'].mean() / 8
    df_2017['B'] = df_2017['B'] + (np.sum(df_2017['B']) / np.sum(df_2017['Rounds'])) * df_2017['Rounds'].mean() / 8
    df_2017['DB'] = df_2017['DB'] + (np.sum(df_2017['DB']) / np.sum(df_2017['Rounds'])) * df_2017['Rounds'].mean() / 8
    df_2017['Rounds'] = df_2017['Rounds'] + df_2017['Rounds'].mean() / 8

    df_2018['P3b'] = df_2018['P3b'] + (np.sum(df_2018['P3b']) / np.sum(df_2018['P3H'])) * df_2018['P3H'].mean() / 8
    df_2018['P3H'] = df_2018['P3H'] + df_2018['P3H'].mean() / 8
    df_2018['P4b'] = df_2018['P4b'] + (np.sum(df_2018['P4b']) / np.sum(df_2018['P4H'])) * df_2018['P4H'].mean() / 8
    df_2018['P4e'] = df_2018['P4e'] + (np.sum(df_2018['P4e']) / np.sum(df_2018['P4H'])) * df_2018['P4H'].mean() / 8
    df_2018['P4H'] = df_2018['P4H'] + df_2018['P4H'].mean() / 8
    df_2018['P5b'] = df_2018['P5b'] + (np.sum(df_2018['P5b']) / np.sum(df_2018['P5H'])) * df_2018['P5H'].mean() / 8
    df_2018['P5e'] = df_2018['P5e'] + (np.sum(df_2018['P5e']) / np.sum(df_2018['P5H'])) * df_2018['P5H'].mean() / 8
    df_2018['P5H'] = df_2018['P5H'] + df_2018['P5H'].mean() / 8
    df_2018['B'] = df_2018['B'] + (np.sum(df_2018['B']) / np.sum(df_2018['Rounds'])) * df_2018['Rounds'].mean() / 8
    df_2018['DB'] = df_2018['DB'] + (np.sum(df_2018['DB']) / np.sum(df_2018['Rounds'])) * df_2018['Rounds'].mean() / 8
    df_2018['Rounds'] = df_2018['Rounds'] + df_2018['Rounds'].mean() / 8

    df_2019['P3b'] = df_2019['P3b'] + (np.sum(df_2019['P3b']) / np.sum(df_2019['P3H'])) * df_2019['P3H'].mean() / 8
    df_2019['P3H'] = df_2019['P3H'] + df_2019['P3H'].mean() / 8
    df_2019['P4b'] = df_2019['P4b'] + (np.sum(df_2019['P4b']) / np.sum(df_2019['P4H'])) * df_2019['P4H'].mean() / 8
    df_2019['P4e'] = df_2019['P4e'] + (np.sum(df_2019['P4e']) / np.sum(df_2019['P4H'])) * df_2019['P4H'].mean() / 8
    df_2019['P4H'] = df_2019['P4H'] + df_2019['P4H'].mean() / 8
    df_2019['P5b'] = df_2019['P5b'] + (np.sum(df_2019['P5b']) / np.sum(df_2019['P5H'])) * df_2019['P5H'].mean() / 8
    df_2019['P5e'] = df_2019['P5e'] + (np.sum(df_2019['P5e']) / np.sum(df_2019['P5H'])) * df_2019['P5H'].mean() / 8
    df_2019['P5H'] = df_2019['P5H'] + df_2019['P5H'].mean() / 8
    df_2019['B'] = df_2019['B'] + (np.sum(df_2019['B']) / np.sum(df_2019['Rounds'])) * df_2019['Rounds'].mean() / 8
    df_2019['DB'] = df_2019['DB'] + (np.sum(df_2019['DB']) / np.sum(df_2019['Rounds'])) * df_2019['Rounds'].mean() / 8
    df_2019['Rounds'] = df_2019['Rounds'] + df_2019['Rounds'].mean() / 8

    # Add suffixes so we can combine them on the indices
    df_2017 = df_2017.add_suffix('_2017')
    df_2018 = df_2018.add_suffix('_2018')
    df_2019 = df_2019.add_suffix('_2019')

    # Join the three years
    df_stats = df_2017.join(df_2018, how='outer').join(df_2019, how='outer')

    # need to fill in NaNs with 0s
    df_stats = df_stats.fillna(0)

    # Assign the weights for recent relevancy
    weight_2017 = 1
    weight_2018 = 2
    weight_2019 = 4

    df_stats['Real_Rounds'] = df_stats['Rounds_2017'] + df_stats['Rounds_2018'] + df_stats['Rounds_2019']
    df_stats['B'] = df_stats['B_2017'] * weight_2017 + df_stats['B_2018'] * weight_2018 + df_stats['B_2019'] * weight_2019
    df_stats['DB'] = df_stats['DB_2017'] * weight_2017 + df_stats['DB_2018'] * weight_2018 + df_stats['DB_2019'] * weight_2019
    df_stats['Rounds'] = df_stats['Rounds_2017'] * weight_2017 + df_stats['Rounds_2018'] * weight_2018 + df_stats['Rounds_2019'] * weight_2019
    df_stats['P3b'] = df_stats['P3b_2017'] * weight_2017 + df_stats['P3b_2018'] * weight_2018 + df_stats['P3b_2019'] * weight_2019
    df_stats['P3H'] = df_stats['P3H_2017'] * weight_2017 + df_stats['P3H_2018'] * weight_2018 + df_stats['P3H_2019'] * weight_2019
    df_stats['P4e'] = df_stats['P4e_2017'] * weight_2017 + df_stats['P4e_2018'] * weight_2018 + df_stats['P4e_2019'] * weight_2019
    df_stats['P4H'] = df_stats['P4H_2017'] * weight_2017 + df_stats['P4H_2018'] * weight_2018 + df_stats['P4H_2019'] * weight_2019
    df_stats['P4b'] = df_stats['P4b_2017'] * weight_2017 + df_stats['P4b_2018'] * weight_2018 + df_stats['P4b_2019'] * weight_2019
    df_stats['P5e'] = df_stats['P5e_2017'] * weight_2017 + df_stats['P5e_2018'] * weight_2018 + df_stats['P5e_2019'] * weight_2019
    df_stats['P5H'] = df_stats['P5H_2017'] * weight_2017 + df_stats['P5H_2018'] * weight_2018 + df_stats['P5H_2019'] * weight_2019
    df_stats['P5b'] = df_stats['P5b_2017'] * weight_2017 + df_stats['P5b_2018'] * weight_2018 + df_stats['P5b_2019'] * weight_2019

    # Only take the columns we want
    df_stats = df_stats[['Rounds', 'B', 'DB', 'P3b', 'P3H', 'P4e', 'P4b', 'P4H', 'P5e', 'P5b', 'P5H']]

    # Save the final stats
    timestr = time.strftime("%Y-%m-%d")
    df_stats.to_pickle('../stats/combined/' + timestr + 'reg.pkl')


if __name__ == '__main__':
    main()
