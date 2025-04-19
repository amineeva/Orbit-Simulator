from orbital_system_sim import SpaceObject, Planet, Satellite, Star, OrbitalSystem, PlanetaryOrbitalSystem, StellarOrbitalSystem
import simulate_orbits
import data_wrangling
import visualization

# central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
# orbiting_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
# system = OrbitalSystem("Test system", central_object)
# system.add_orbiting_object(orbiting_object)

# central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
# orbiting_object = Star("Proxima Centuari", 107292.36, 1.989e30*0.1221, 0, 0, 0, 3.828e26*0.0017, "Red Dwarf")
# system = OrbitalSystem("Test system", central_object)
# system.add_orbiting_object(orbiting_object)


# central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
# orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
# orbiting_object_2 = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
# mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
# phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid") # creating Martian planet moons as satellite instances
# deimos_moon = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
# mars_system = PlanetaryOrbitalSystem("Mars system", mars_planet) # creating Mars orbit system 
# system = OrbitalSystem("Test system", central_object)
# system.add_orbiting_object(orbiting_object_1)
# system.add_orbiting_object(orbiting_object_2)
# system.add_orbiting_object(mars_system)
# system.add_orbiting_object(orbiting_object_1)

# print(system.orbiting_objects_list())

central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
system = OrbitalSystem("Test system", central_object)
# system.add_orbiting_object(orbiting_object_1)
print(system.get_orbital_period("Mars"))