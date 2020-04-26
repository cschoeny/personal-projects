import itertools
import lib.LP_solver as lps
from math import log


class Event():
    """
    The event class holds all the fights.
    """

    def __init__(self, *args):
        self.fights = [arg for arg in args]

    def get_event_outcomes(self):
        return [fight.get_outcomes() for fight in self.fights]

    def highest_odds_all_win(self):
        """
        First we get a list of lists. Each inner list is a tuple with a fighters name salary and odds to win.
        Then we will iterate through each combination of possible sets of winners, and then use LP to find the highest prob given that set.
        Then we will take the overall highest prob. This way is algorithmically more efficient than cycling through all possible lineups.
        """
        list_of_fighters = [[(fight.Fighter_A.name, fight.Fighter_A.salary, fight.normalize_odds([fight.odds_A['win'], fight.odds_B['win']])[0]),
                             (fight.Fighter_B.name, fight.Fighter_B.salary, fight.normalize_odds([fight.odds_A['win'], fight.odds_B['win']])[1])]
                            for fight in self.fights]

        all_outcomes = list(itertools.product(*list_of_fighters))

        # Now we need to step through each outcome, and run an LP on it.
        # Can re-use existing LP function, but put in log odds instead of points.
        best_odds = log(.00001)
        for cur_event in all_outcomes:
            names = [fighter[0] for fighter in cur_event]
            salaries = [fighter[1] for fighter in cur_event]
            log_odds = [log(fighter[2]) for fighter in cur_event]

            cur_names, cur_odds = lps.event_nuts(names, salaries, log_odds, verbose=1)
            if isinstance(cur_names, list):
                if len(cur_names) == 6:
                    if cur_odds > best_odds:
                        best_names = cur_names
                        best_odds = cur_odds
        return best_names, best_odds

    def highest_odds_all_itd(self):
        """
        First we get a list of lists. Each inner list is a tuple with a fighters name salary and odds to win.
        Then we will iterate through each combination of possible sets of winners, and then use LP to find the highest prob given that set.
        Then we will take the overall highest prob. This way is algorithmically more efficient than cycling through all possible lineups.
        """
        def get_itd_odds(fight, fighter):
            if fighter == 'A':
                win, _ = fight.normalize_odds([fight.odds_A['win'], fight.odds_B['win']])
                KO, SUB, _ = fight.normalize_odds([fight.odds_A['KO/TKO'], fight.odds_A['SUB'], fight.odds_A['DEC']])
            elif fighter == 'B':
                KO, SUB, _ = fight.normalize_odds([fight.odds_B['KO/TKO'], fight.odds_B['SUB'], fight.odds_B['DEC']])
                _, win = fight.normalize_odds([fight.odds_A['win'], fight.odds_B['win']])
            else:
                raise NameError('bad fighter name in get_itd_odds')
            return win*(KO+SUB)

        list_of_fighters = [[(fight.Fighter_A.name, fight.Fighter_A.salary, get_itd_odds(fight, 'A')),
                             (fight.Fighter_B.name, fight.Fighter_B.salary, get_itd_odds(fight, 'B'))]
                            for fight in self.fights]

        all_outcomes = list(itertools.product(*list_of_fighters))

        # Now we need to step through each outcome, and run an LP on it.
        # Can re-use existing LP function, but put in log odds instead of points.
        best_odds = log(.00001)
        for cur_event in all_outcomes:
            names = [fighter[0] for fighter in cur_event]
            salaries = [fighter[1] for fighter in cur_event]
            log_odds = [log(fighter[2]) for fighter in cur_event]

            cur_names, cur_odds = lps.event_nuts(names, salaries, log_odds, verbose=1)
            # if len(cur_names == 6):
            if cur_odds > best_odds:
                best_names = cur_names
                best_odds = cur_odds
        return best_names, best_odds
