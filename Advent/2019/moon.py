class Moon:

    def __init__(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.pos_z = pos[2]
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    @property
    def potential(self):
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    @property
    def kinetic(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    @property
    def total_energy(self):
        return self.potential * self.kinetic
