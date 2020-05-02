from moon import Moon
from orbits import Orbits

Io = Moon([3, 2, -6])
Europa = Moon([-13, 18, 10])
Ganymede = Moon([-8, -1, 13])
Callisto = Moon([5, 10, 4])

orbit = Orbits(1000, Io, Europa, Ganymede, Callisto)
orbit.evolve()
print(orbit.total_energy_system())



############ Part 2
from moon import Moon
from orbits import Orbits

Io = Moon([3, 2, -6])
Europa = Moon([-13, 18, 10])
Ganymede = Moon([-8, -1, 13])
Callisto = Moon([5, 10, 4])

orbit = Orbits(_, Io, Europa, Ganymede, Callisto)
orbit.evolve_check_prev()
