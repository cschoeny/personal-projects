# The purpose of this file is to filter our database down to just the golfers in the draftkings contest.
import pandas as pd
import time


def main():
    timestr = time.strftime("%Y-%m-%d")
    df_stats = pd.read_pickle('../stats/combined/' + timestr + 'reg.pkl')

    # Read in draftkings
    df_dk = pd.read_csv('../raw_data/contests/' + timestr + '.csv', index_col='Name', usecols=['Name', 'Salary'])

    # need to change some names to match to draftkings
    new_names = {'Charles Howell III': 'Charles Howell',
                 'Rafa Cabrera Bello': 'Rafael Cabrera-Bello',
                 'Harold Varner III': 'Harold Varner',
                 'Billy Hurley III': 'Billy Hurley',
                 'Fabián Gómez': 'Fabian Gomez',
                 'Alex Noren': 'Alexander Noren',
                 'HaoTong Li': 'Hao-Tong Li',
                 'Byeong Hun An': 'Byeong-Hun An',
                 'Sangmoon Bae': 'Sang-Moon Bae',
                 'Xinjun Zhang': 'Xin-Jun Zhang'}
    df_stats = df_stats.rename(index=new_names)

    # Merge dk with stats
    df = df_dk.join(df_stats)

    # column to indicate that it used to have nans
    df['Real'] = df['B'].notnull()

    # need to fill in NaNs (this is sorted by price already, so those around it should make sense)
    df = df.fillna(method='ffill')

    # Export the file for the Monte Carlo simulation.
    df.to_pickle('../stats/with_prices/' + timestr + 'reg.pkl')


if __name__ == '__main__':
    main()
