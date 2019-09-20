class Event():
    """
    The event class holds all the fights.
    """

    def __init__(self, *args):
        self.fights = [arg for arg in args]

    def get_event_outcomes(self):
        return [fight.get_outcomes() for fight in self.fights]
