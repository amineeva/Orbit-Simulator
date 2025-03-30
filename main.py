# Run project from this file
from orbital_system_sim import Planet
from orbital_system_sim import Satellite
import visualization

# trying to create a Mars instance
mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
print(mars_planet)

phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 6000, 100, "asteroid")

mars_planet.add_moon(phobos_moon)

print("")
print(mars_planet.moon_list)