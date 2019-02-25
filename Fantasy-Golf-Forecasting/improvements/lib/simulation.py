import pandas as pd
import numpy as np
import time
from scipy.stats import rankdata
import pdb


def sim_conditions(par3=4, par4=10, par5=4, sims=1000):
    timestr = time.strftime("%Y-%m-%d")
    df = pd.read_pickle('../stats/with_prices/' + timestr + 'reg.pkl')

    par = 3 * par3 + 4 * par4 + 5 * par5
    # If these don't add up raise an exception
    if par3 + par4 + par5 != 18:
        raise NameError('Pars dont add up to 18')

    # %% Set the draftkings scoring system
    pts_b = 3
    pts_e = 8
    pts_p = 0.5
    pts_B = -0.5
    pts_DB = -1

    pts_streak = 3
    pts_BF = 3
    pts_4U70 = 5

    def pts_place_tmp(plc):
        if plc > 50:
            return 0
        if plc > 40:
            return 1
        if plc > 30:
            return 2
        if plc > 25:
            return 3
        if plc > 20:
            return 4
        if plc > 15:
            return 5
        if plc > 10:
            return 6
        if plc == 10:
            return 7
        if plc == 9:
            return 8
        if plc == 8:
            return 9
        if plc == 7:
            return 10
        if plc == 6:
            return 12
        if plc == 5:
            return 14
        if plc == 4:
            return 16
        if plc == 3:
            return 18
        if plc == 2:
            return 20
        if plc == 1:
            return 30

    pts_place = np.vectorize(pts_place_tmp)  # This makes it element wise for np.arrays

    # The following probabilities were found through separate code (availabile in the top level of the repo)
    streak_prob = {0: 0, 1: 0, 2: 0, 3: 0.01936, 4: 0.07377, 5: 0.17107, 6: 0.31648, 7: 0.49038, 8: 0.673, 9: 0.82751, 10: 0.9343, 11: 0.98388, 12: 0.99847, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1}

    # %% Calculate poisson rates
    df['B/R'] = df['B'].div(df['Rounds'])
    df['DB/R'] = df['DB'].div(df['Rounds'])
    df['3b/H'] = df['P3b'].div(df['P3H'])
    df['4e/H'] = df['P4e'].div(df['P4H'])
    df['4b/H'] = df['P4b'].div(df['P4H'])
    df['5e/H'] = df['P5e'].div(df['P5H'])
    df['5b/H'] = df['P5b'].div(df['P5H'])

    num_players, tmp = df.shape
    birdies = np.empty([num_players, sims, 4])
    for player_idx in range(num_players):
        cur_birdies3 = np.random.poisson(df.iloc[player_idx]['3b/H'] * par3, [1, sims, 4])
        cur_birdies4 = np.random.poisson(df.iloc[player_idx]['4b/H'] * par4, [1, sims, 4])
        cur_birdies5 = np.random.poisson(df.iloc[player_idx]['5b/H'] * par5, [1, sims, 4])
        cur_birdies = cur_birdies3 + cur_birdies4 + cur_birdies5
        birdies[player_idx, :, :] = cur_birdies

    eagles = np.empty([num_players, sims, 4])
    for player_idx in range(num_players):
        cur_eagles4 = np.random.poisson(df.iloc[player_idx]['4e/H'] * par4, [1, sims, 4])
        cur_eagles5 = np.random.poisson(df.iloc[player_idx]['5e/H'] * par5, [1, sims, 4])
        cur_eagles = cur_eagles4 + cur_eagles5
        eagles[player_idx, :, :] = cur_eagles

    bogeys = np.empty([num_players, sims, 4])
    for player_idx in range(num_players):
        cur_bogeys = np.random.poisson(df.iloc[player_idx]['B/R'], [1, sims, 4])
        bogeys[player_idx, :, :] = cur_bogeys

    doublebogeys = np.empty([num_players, sims, 4])
    for player_idx in range(num_players):
        cur_doublebogeys = np.random.poisson(df.iloc[player_idx]['DB/R'], [1, sims, 4])
        doublebogeys[player_idx, :, :] = cur_doublebogeys

    pars = np.full([num_players, sims, 4], 18)
    pars = pars - birdies - eagles - bogeys - doublebogeys
    pars[pars < 0] = 0

    # %% Get the scores for each round
    scores = np.full([num_players, sims, 4], par)
    scores = scores - birdies - 2 * eagles + bogeys + 2 * doublebogeys

    # %% cut the players
    made_cut = np.empty([num_players, sims])
    for cur_sim in range(sims):
        after2 = np.sum(scores[:, cur_sim, 0:2], axis=1)
        made_cut[:, cur_sim] = rankdata(after2, method='min') <= 70
    missed_cut = (made_cut - 1) * (-1)

    # Calculate the total dk_score
    dk_scores = np.zeros([num_players, sims, 4])
    # first lets calculate just normal points
    dk_scores = pts_b * birdies + pts_e * eagles + pts_B * bogeys + pts_DB * doublebogeys + pts_p * pars

    # now lets add the streak bonus
    def streak_bonus_tmp(be):
        prob = streak_prob[be]
        return np.random.binomial(1, prob)
    streak_bonus = np.vectorize(streak_bonus_tmp)
    bir_eag = birdies + eagles
    bir_eag[bir_eag > 18] = 18  # need to cap it at 18
    streak_pts = streak_bonus(bir_eag)
    dk_scores = dk_scores + streak_pts * pts_streak  # adds the streak to each day that has it

    # need to add bogey free bonus
    bogeyFree = 1 * (bogeys == 0)
    doublebogeyFree = 1 * (doublebogeys == 0)
    allBFree = bogeyFree * doublebogeyFree
    dk_scores = dk_scores + pts_BF * allBFree

    # now lets add the placement bonus
    total_score = np.sum(scores, axis=2)
    # need to make sure we dont give placement bonuses to those missing the cut so we add 1000 strokes
    total_score = total_score + missed_cut * 1000
    ranking = np.empty([num_players, sims])
    for cur_sim in range(sims):
        ranking[:, cur_sim] = rankdata(total_score[:, cur_sim], method='min')
    dk_placement_score = pts_place(ranking)
    dk_scores[:, :, 0] = dk_scores[:, :, 0] + dk_placement_score  # might as well add it onto the first day

    # Now we need to add a bonus score if players have all 4 rounds below 70
    A4U70_array = np.max(scores, axis=2) < 70
    dk_scores[:, :, 2] = dk_scores[:, :, 2] + A4U70_array * pts_4U70  # we put it in this on the 3rd round so that it gets zeroed out if CUT

    # Now we need to 0 out the scores from days 3 and 4 for those that did not make the cut
    dk_scores[:, :, 2] = dk_scores[:, :, 2] * made_cut
    dk_scores[:, :, 3] = dk_scores[:, :, 3] * made_cut

    # Finally, we compress the scores
    dk_final_score = np.sum(dk_scores, axis=2)
    return dk_final_score, made_cut


def aggregate_results(dk_final_score, made_cut):
    timestr = time.strftime("%Y-%m-%d")
    df_dk = pd.read_pickle('../stats/with_prices/' + timestr + 'reg.pkl')
    # %% Now let's calculate the statistics of importance
    dk_median = np.median(dk_final_score, axis=1)
    dk_mean = np.mean(dk_final_score, axis=1)
    dk_max = np.max(dk_final_score, axis=1)
    dk_min = np.min(dk_final_score, axis=1)
    dk_25 = np.percentile(dk_final_score, 25, axis=1)
    dk_75 = np.percentile(dk_final_score, 75, axis=1)
    dk_makecut = np.mean(made_cut, axis=1)

    # %% Now let's create the dataframe that we will pass to the linear program
    df_results = pd.DataFrame(index=df_dk.index.copy())
    df_results['Salary'] = df_dk['Salary']
    df_results['dk_max'] = dk_max
    df_results['dk_min'] = dk_min
    df_results['dk_median'] = dk_median
    df_results['dk_mean'] = dk_mean
    df_results['dk_75'] = dk_75
    df_results['dk_25'] = dk_25
    df_results['dk_makecut'] = dk_makecut
    df_results['Rounds'] = df_dk['Real_Rounds']
    df_results['Have_Data'] = df_dk['Real']

    df_results.to_pickle('../stats/sim_results/results_' + timestr + '.pkl')
