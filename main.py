# Run project from this file
from orbital_system_sim import Planet, Satellite, Star, PlanetaryOrbitalSystem, StellarOrbitalSystem
import simulate_orbits
import data_wrangling
import visualization
import pandas as pd

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

# solar system - PLANETS ONLY
solar_system_p = StellarOrbitalSystem("Solar System", sun)
solar_system_p.add_orbiting_object(mars_planet)
solar_system_p.add_orbiting_object(mercury_planet)

# print(solar_system_p)
# print(solar_system_p.orbiting_objects_list())

# print(solar_system_p.get_orbit_object_distance("Mercury"))

# simulation testing
ss_planet_positions, ss_time_p = simulate_orbits.run_simulation(solar_system_p)

# printing dataframe
ss_positions_p = data_wrangling.convert_simulation_to_dataframe(ss_planet_positions, ss_time_p)
# print(ss_positions)

# plot simulation - ONLY PLANETS, operational
# visualization.plot_object(ss_positions, "Mars") # one object within system
# visualization.plot_system(solar_system_p, ss_positions) #full system, default X position
# visualization.plot_system(solar_system_p, ss_positions, "Time", "Y_pos") # full system, set y position



# vvvvvvvvvvvvv TEST SECTION - testing the code with orbital systems within orbital systems 
# solar system - PLANETS AND ORBITAL SYSTEMS
solar_system = StellarOrbitalSystem("Solar System", sun)
solar_system.add_orbiting_object(mars_system)
solar_system.add_orbiting_object(mercury_planet)
print(mars_system)
print("")
print(solar_system)
print("")
print(solar_system.orbiting_objects_list())

print(solar_system.get_orbit_object_distance("Mercury"))
print("")
print(solar_system.get_orbit_object_distance("Mars system"))

# simulation testing
ss_positions_system, ss_time_s = simulate_orbits.run_simulation(solar_system)

ss_positions_s = data_wrangling.convert_simulation_to_dataframe(ss_positions_system, ss_time_s)
print(ss_positions_s["Object"].unique()) # I need the 'Mars System' to be split into all objects in the mars system
visualization.plot_object(ss_positions_s, "Mars system") # one object within system
visualization.plot_system(solar_system, ss_positions_s) #full system, default X position
visualization.plot_system(solar_system, ss_positions_s, "Time", "Y_pos") # full system, set y position


