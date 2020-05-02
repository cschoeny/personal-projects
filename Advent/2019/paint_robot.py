class PRobot:

    def __init__(self):
        self.init_color = 'B'
        self.x = 0
        self.y = 0
        self.dir = 'U'
        self.clockwise = {'U': 'R',
                          'R': 'D',
                          'D': 'L',
                          'L': 'U'}
        self.counterclockwise = {'U': 'L',
                                 'L': 'D',
                                 'D': 'R',
                                 'R': 'U'}
        self.move = {'U': (0, 1),
                     'R': (1, 0),
                     'D': (0, -1),
                     'L': (-1, 0)}
        self.colors = {}
        self.switch_count = 0

    def action_color(self, color_int):
        # Let's try only adding after it is white
        if self.cur_loc not in self.colors:
            if color_int == 0:
                pass
            elif color_int == 1:
                self.colors[self.cur_loc] = 'W'
            else:
                raise ValueError('Non binary input to action_color')
        else:
            if color_int == 0:
                self.colors[self.cur_loc] = 'B'
            elif color_int == 1:
                self.colors[self.cur_loc] = 'W'
            else:
                raise ValueError('Non binary input to action_color')

    def action_move(self, direction_int):
        if direction_int == 0:
            self.dir = self.counterclockwise[self.dir]
        elif direction_int == 1:
            self.dir = self.clockwise[self.dir]
        else:
            raise ValueError('Non binary input to direction_int')
        self.x += self.move[self.dir][0]
        self.y += self.move[self.dir][1]

    def output_current_color(self):
        # 0: Black (default)
        # 1: White
        if self.cur_loc in self.colors:
            if self.colors[self.cur_loc] == 'B':
                return 0
            else:
                return 1
        return 0

    @property
    def cur_loc(self):
        return (self.x, self.y)
