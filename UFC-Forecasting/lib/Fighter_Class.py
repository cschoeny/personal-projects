import pandas as pd
import os
import numpy as np
from sklearn.neighbors import KernelDensity


class Fighter():
    """
    The main purpose of the Fighter class is to be able to sample DK_Points for a specific fighter given specific victory conditions.
    """

    def __init__(self, weight_class, five_round=False):
        self.weight_class = weight_class
        self.five_round = five_round

        self.MIN_SAMPLES = 25
        self.dec_round_cat = self.load_dec_round_cat()

        self.df = self.load_df()
        self.WC_kernel_dict = self.create_WC_kernel_dict()
        self.kernel_dict = self.create_kernel_dict()

    def input_checks(self, method, round):
        if self.weight_class not in ["Welterweight",
                                     "Lightweight",
                                     "Featherweight",
                                     "Middleweight",
                                     "Bantamweight",
                                     "Light Heavyweight",
                                     "Heavyweight",
                                     "Women's Strawweight",
                                     "Flyweight",
                                     "Women's Bantamweight",
                                     "Women's Flyweight",
                                     "Women's Featherweight",
                                     "Catch Weight"]:
            raise ValueError('Invalid Weight Class name')

        if method not in ['DEC', 'KO/TKO', 'SUB']:
            raise ValueError('Invalid Method name')

        if method in ['KO/TKO', 'SUB'] and round not in ['1', '2', '3', '4', '5']:
            raise ValueError('Invalid Round name')

    def load_df(self):
        dirname = os.path.abspath('')
        filename_pkl = dirname + "/data/combined_stats.pkl"
        return pd.read_pickle(filename_pkl)

    def load_dec_round(self):
        if self.five_round:
            return '5 DEC'
        else:
            return '3 DEC'

    def sample_DK_Points(self, method, round=None):
        """
        First try with weight class, and if not evnough significant data points, then average with dropped weight class.
        """
        self.input_checks(method, round)
        if method in ['KO/TKO', 'SUB']:
            if self.df.loc[(self.df['Weight class'] == self.weight_class) & (self.df['Round_Cat'] == round) & (self.df['Method'] == method), 'DK_Points'].shape[0] > self.MIN_SAMPLES:
                return self.WC_kernel_dict[method][round].sample()
            else:
                return np.mean([self.WC_kernel_dict[method][round].sample(), self.kernel_dict[method][round].sample()])
        else:
            if self.df.loc[(self.df['Weight class'] == self.weight_class) & (self.df['Round_Cat'] == self.dec_round_cat), 'DK_Points'].shape[0] > self.MIN_SAMPLES:
                return self.WC_kernel_dict['DEC'].sample()
            else:
                return np.mean([self.WC_kernel_dict['DEC'].sample(), self.kernel_dict['DEC'].sample()])

    def create_WC_kernel_dict(self):
        # WILL NEED to come back and handle cases where x is empty.
        WC_kernel_dict = {}
        methods = ['KO/TKO', 'SUB']
        if self.five_round:
            rounds = ['1', '2', '3', '4', '5']
        else:
            rounds = ['1', '2', '3']
        for method in methods:
            WC_kernel_dict[method] = {}
            for round in rounds:
                x = np.array(self.df.loc[(self.df['Weight class'] == self.weight_class) & (self.df['Round_Cat'] == round) & (self.df['Method'] == method), 'DK_Points']).reshape(-1, 1)
                kde = KernelDensity().fit(x)
                WC_kernel_dict[method][round] = kde

        WC_kernel_dict['DEC'] = np.array(self.df.loc[(self.df['Weight class'] == self.weight_class) & (self.df['Round_Cat'] == self.dec_round_cat), 'DK_Points']).reshape(-1, 1)

        return WC_kernel_dict

    def create_kernel_dict(self):
        kernel_dict = {}
        methods = ['KO/TKO', 'SUB']
        if self.five_round:
            rounds = ['1', '2', '3', '4', '5']
        else:
            rounds = ['1', '2', '3']
        for method in methods:
            kernel_dict[method] = {}
            for round in rounds:
                x = np.array(self.df.loc[(self.df['Round'] == round) & (self.df['Method'] == method), 'DK_Points']).reshape(-1, 1)
                kde = KernelDensity().fit(x)
                kernel_dict[method][round] = kde

        kernel_dict['DEC'] = np.array(self.df.loc[self.df['Round_Cat'] == self.dec_round_cat, 'DK_Points']).reshape(-1, 1)

        return kernel_dict
