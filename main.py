# Run project from this file
from orbital_system_sim import Planet, Satellite, Star, PlanetaryOrbitalSystem, StellarOrbitalSystem
import visualization

# creating planets
mercury_planet = Planet("Mercury", 100, 100, 0, 0, 0, 0.3, "rocky")
mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")

# creating Martian planet moons as satellite instances
phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 6000, 100, "asteroid")
deimos_moon = Satellite("Deimos", 11, 0, 0, 0, 0, 6000, 100, "asteroid")

# creating Mars orbit system 
mars_system = PlanetaryOrbitalSystem("Mars system", mars_planet)
mars_system.add_moon(phobos_moon)
mars_system.add_moon(deimos_moon)

# creating Sun
sun = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")

# creating solar system
solar_system = StellarOrbitalSystem("Solar System", sun)
solar_system.add_orbiting_object(mars_system)
solar_system.add_orbiting_object(mercury_planet)

print(solar_system)
print(solar_system.orbiting_objects_list())





