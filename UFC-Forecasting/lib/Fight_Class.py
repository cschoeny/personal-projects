import random


class Fight():
    """
    We will instantiate a Fight between two fighters.
    """

    def __init__(self, Fighter_A, odds_A, Fighter_B, odds_B, num_fights):
        self.Fighter_A = Fighter_A
        self.odds_A = odds_A
        self.Fighter_B = Fighter_B
        self.odds_B = odds_B
        self.num_fights = num_fights
        self.five_round = Fighter_A.five_round
        self.num_rounds_dec = self.num_rounds_dec()
        self.check_consistency()

    def check_consistency(self):
        if self.Fighter_A.five_round != self.Fighter_B.five_round:
            raise ValueError("The fighters don't agree on the number of rounds.")

    def num_rounds_dec(self):
        if self.Fighter_A.five_round:
            return '5 DEC'
        else:
            return '3 DEC'

    def convert_to_prob(self, odds):
        """
        Converts American odds (strings in list) to probabilities (not normalized)
        """
        prob_odds = []
        for odd in odds:
            if odd[0] == '+':
                prob = 100 / (100 + int(odd[1:]))
            elif odd[0] == '-':
                prob = int(odd[1:]) / (100 + int(odd[1:]))
            else:
                raise ValueError('probabilities in convert_to_prob not formatting correctly.')
            prob_odds.append(prob)
        return prob_odds

    def normalize_odds(self, odds):
        """
        Given any number of American Odds (as strings in a list) it converts them to probabilities.
        """
        prob_odds = self.convert_to_prob(odds)
        return [prob / sum(prob_odds) for prob in prob_odds]

    def choose_winner(self, odds_win_A, odds_win_B):
        fighters = [self.Fighter_A.name, self.Fighter_B.name]
        odds = [odds_win_A, odds_win_B]
        return random.choices(fighters, odds, k=self.num_fights)

    def choose_method(self, odds_DEC, odds_KO, odds_SUB, num_wins):
        methods = ['DEC', 'KO/TKO', 'SUB']
        odds = [odds_DEC, odds_KO, odds_SUB]
        return random.choices(methods, odds, k=num_wins)

    def choose_round(self, round_odds, num_stoppages):
        if self.five_round:
            rounds = ['1', '2', '3', '4', '5']
        else:
            rounds = ['1', '2', '3']
        return random.choices(rounds, round_odds, k=num_stoppages)

    def get_outcomes(self):
        """
        This functoin returns a list of lists where each inner list consists of:
        [winner's_name, winning_method, winning_round]
        """
        # First let's produce a list of winners
        winning_odds = self.normalize_odds([self.odds_A['win'], self.odds_B['win']])
        winners = self.choose_winner(*winning_odds)

        # Now let's produce a list, per fighter, with the method of winning
        methods_A_odds = self.normalize_odds([self.odds_A['DEC'], self.odds_A['KO/TKO'], self.odds_A['SUB']])
        methods_A = self.choose_method(*methods_A_odds, num_wins=winners.count(self.Fighter_A.name))

        methods_B_odds = self.normalize_odds([self.odds_B['DEC'], self.odds_B['KO/TKO'], self.odds_B['SUB']])
        methods_B = self.choose_method(*methods_B_odds, num_wins=winners.count(self.Fighter_B.name))

        # Now let's produce the rounds for stoppages
        if self.five_round:
            rounds_list = ['1', '2', '3', '4', '5']
        else:
            rounds_list = ['1', '2', '3']
        rounds_A_odds = self.normalize_odds([self.odds_A[x] for x in rounds_list])
        rounds_A = self.choose_round(rounds_A_odds, num_stoppages=(methods_A.count('KO/TKO') + methods_A.count('SUB')))

        rounds_B_odds = self.normalize_odds([self.odds_B[x] for x in rounds_list])
        rounds_B = self.choose_round(rounds_B_odds, num_stoppages=(methods_B.count('KO/TKO') + methods_B.count('SUB')))

        # Now need to produce the overall list
        methods_A = iter(methods_A)
        methods_B = iter(methods_B)
        rounds_A = iter(rounds_A)
        rounds_B = iter(rounds_B)

        overall = []
        for winner in winners:
            inner = [winner]
            if winner == self.Fighter_A.name:
                inner.append(next(methods_A))
                if inner[-1] == 'DEC':
                    inner.append(self.num_rounds_dec)
                else:
                    inner.append(next(rounds_A))
                inner.append(self.Fighter_A.sample_DK_Points(inner[1], inner[2]))
            else:  # Fighter_B wins
                inner.append(next(methods_B))
                if inner[-1] == 'DEC':
                    inner.append(self.num_rounds_dec)
                else:
                    inner.append(next(rounds_B))
                inner.append(self.Fighter_B.sample_DK_Points(inner[1], inner[2]))
            overall.append(inner)

        return overall
