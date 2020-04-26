from functools import reduce
from math import gcd


class Orbits:

    def __init__(self, steps, *moons):

        self.steps = steps
        self.moons = list(moons)
        self.initial_state_x = self.get_current_state_x
        self.initial_state_y = self.get_current_state_y
        self.initial_state_z = self.get_current_state_z
        self.num_steps = 0

    def evolve(self):
        for _ in range(self.steps):
            for current_moon in self.moons:
                for other_moon in self.moons:
                    self.update_velocity(current_moon, other_moon)
            for current_moon in self.moons:
                self.update_position(current_moon)

    def evolve_check_prev(self):
        x_period = 0
        y_period = 0
        z_period = 0
        while True:
            self.num_steps += 1
            for current_moon in self.moons:
                for other_moon in self.moons:
                    self.update_velocity(current_moon, other_moon)
            for current_moon in self.moons:
                self.update_position(current_moon)
            if self.get_current_state_x == self.initial_state_x and x_period == 0:
                x_period = self.num_steps
                print(f'x period = {x_period}')
            if self.get_current_state_y == self.initial_state_y and y_period == 0:
                y_period = self.num_steps
                print(f'y period = {y_period}')
            if self.get_current_state_z == self.initial_state_z and z_period == 0:
                z_period = self.num_steps
                print(f'z period = {z_period}')
            if x_period != 0 and y_period != 0 and z_period != 0:
                return self.lcmm(x_period, y_period, z_period)

    def update_velocity(self, moon1, moon2):
        if moon1.pos_x < moon2.pos_x:
            moon1.vel_x += 1
        elif moon1.pos_x > moon2.pos_x:
            moon1.vel_x -= 1
        if moon1.pos_y < moon2.pos_y:
            moon1.vel_y += 1
        elif moon1.pos_y > moon2.pos_y:
            moon1.vel_y -= 1
        if moon1.pos_z < moon2.pos_z:
            moon1.vel_z += 1
        elif moon1.pos_z > moon2.pos_z:
            moon1.vel_z -= 1

    def update_position(self, moon):
        moon.pos_x += moon.vel_x
        moon.pos_y += moon.vel_y
        moon.pos_z += moon.vel_z

    def total_energy_system(self):
        return sum(moon.total_energy for moon in self.moons)

    @property
    def get_current_state_x(self):
        moon_coords = []
        for moon in self.moons:
            moon_coords.append([moon.pos_x, moon.vel_x])
        return tuple(moon_coords)

    @property
    def get_current_state_y(self):
        moon_coords = []
        for moon in self.moons:
            moon_coords.append([moon.pos_y, moon.vel_y])
        return tuple(moon_coords)

    @property
    def get_current_state_z(self):
        moon_coords = []
        for moon in self.moons:
            moon_coords.append([moon.pos_z, moon.vel_z])
        return tuple(moon_coords)

    def lcm(self, a, b):
        return a * b // gcd(a, b)

    def lcmm(self, *args):
        return reduce(self.lcm, args)
