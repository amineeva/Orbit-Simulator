from orbital_system_sim import SpaceObject, Planet, Satellite, Star, OrbitalSystem, PlanetaryOrbitalSystem, StellarOrbitalSystem
import simulate_orbits
import data_wrangling
import visualization

central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
orbiting_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
system = OrbitalSystem("Test system", central_object)
system.add_orbiting_object(orbiting_object)



print(system.orbiting_objects_list())