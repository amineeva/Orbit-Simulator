# Run project from this file
from orbital_system_sim import SpaceObject, Planet, Satellite, Star, OrbitalSystem, PlanetaryOrbitalSystem, StellarOrbitalSystem
import simulate_orbits
import data_wrangling
import visualization
import pandas as pd
import numpy as np

# test set-up
mercury_planet = Planet("Mercury", 100, 100, 0, 0, 0, 0.3, "rocky") # creating planets
mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid") # creating Martian planet moons as satellite instances
deimos_moon = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
mars_system = PlanetaryOrbitalSystem("Mars system", mars_planet) # creating Mars orbit system 
mars_system.add_orbiting_object(phobos_moon)
mars_system.add_orbiting_object(deimos_moon)
sun = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type") # creating Sun

# solar system - PLANETS ONLY
solar_system_p = StellarOrbitalSystem("Solar System", sun)
solar_system_p.add_orbiting_object(mars_planet)
solar_system_p.add_orbiting_object(mercury_planet)

# print(solar_system_p)
# print(solar_system_p.orbiting_objects_list())

# print(solar_system_p.get_orbit_object_distance("Mercury"))

# # simulation testing
# ss_planet_positions, ss_time_p = simulate_orbits.run_simulation(solar_system_p)

# # printing dataframe
# ss_positions_p = data_wrangling.convert_simulation_to_dataframe(ss_planet_positions, ss_time_p)
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
print(mars_system.orbiting_objects_list())
print("")
print(solar_system)
print("")
print(solar_system.orbiting_objects_list())
print("")
print(phobos_moon)
print("")
sim_duration = 2
timestep = 0.00273973*7
time = np.linspace(0, sim_duration, round(sim_duration/timestep)) # time vector in years
num_steps = len(time)
positions, velocities, angular_velocities, orbit_radii, parent = simulate_orbits.establish_simulation(solar_system, solar_system.orbiting_objects, time) 
print(positions.keys()) #in its current state this stores the 'mars system' as one object, 'mercury' as one orbject
print(parent)
print(angular_velocities)
print(orbit_radii)

print(solar_system.get_orbit_object_distance("Mercury"))
print("")
print(solar_system.get_orbit_object_distance("Mars system"))

# simulation testing
ss_positions_system, ss_time_s = simulate_orbits.run_simulation(solar_system)

ss_positions_s = data_wrangling.convert_simulation_to_dataframe(ss_positions_system, ss_time_s)
print(ss_positions_s["Object"].unique()) # Prints all unique objects in the solar system
print(ss_positions_s[ss_positions_s["Object"] == "Mars"])
print(ss_positions_s[ss_positions_s["Object"] == "Phobos"])
visualization.plot_object(ss_positions_s, "Mars") # one object within system
visualization.plot_object(ss_positions_s, "Phobos")
visualization.plot_system(solar_system, ss_positions_s) #full system, default X position
visualization.plot_system(solar_system, ss_positions_s, "Time", "Y_pos") # full system, set y position
