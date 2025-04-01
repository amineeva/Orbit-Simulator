# File holds simulation function
import numpy as np
import math
import pandas as pd
from orbital_system_sim import Planet, Satellite, Star, PlanetaryOrbitalSystem, StellarOrbitalSystem, OrbitingObject, OrbitalSystem

def establish_simulation(system, orbiting_objects_dictionary, time):
    """
    Function used within run_simulation in order to create the initial system vectors. Defines intial position conditions. 

    Args:
        orbiting_objects_dictionary: Dictionary of objects, orbiting within system.
        time: Numpy array (vector) holding a timestep-ed time vector in years

    Returns:
        positions: Dictionary for x, y, z positions of each orbiting object
        velocities: Dictionary for x, y, z velocities of each orbiting object
        angular_velocities: Dictionary for angular velocity of each orbiting object
        orbit_radii: Dictionary for distances between system center and each orbiting object
    """
    num_steps = len(time)
    # Dictionaries to store positions, velocities, angular velocities, orbital distance from system center to object
    positions = {}
    velocities = {}
    angular_velocities = {}
    orbit_radii = {}
    for orbit_object_name, orbit_object in orbiting_objects_dictionary.items():
        # this is for the orbiting objects
        if isinstance(orbit_object, OrbitingObject):
            angular_velocities[orbit_object_name] = 2*math.pi/system.get_orbital_period(orbit_object_name)

            positions[orbit_object_name] = np.zeros((num_steps, 3))
            velocities[orbit_object_name] = np.zeros((num_steps, 3))

            positions[orbit_object_name][0] = [orbit_object.start_x, orbit_object.start_y, orbit_object.start_z]
            velocities[orbit_object_name][0] = [0, 0, 0]

            orbit_radii[orbit_object_name] = system.get_orbit_object_distance(orbit_object_name)

        # this is for the orbiting systems - but get_orbital_period should work for OrbitalSystem knstances as well
        # I think the issue here is creating empty dictionaries for each of the orbiting objects within the orbital systems orbiting the main system
        elif isinstance(orbit_object, OrbitalSystem):
            angular_velocities[orbit_object_name] = 2*math.pi/system.get_orbital_period(orbit_object_name)

            positions[orbit_object_name] = np.zeros((num_steps, 3))
            velocities[orbit_object_name] = np.zeros((num_steps, 3))

            positions[orbit_object_name][0] = [orbit_object.start_x, orbit_object.start_y, orbit_object.start_z]
            velocities[orbit_object_name][0] = [0, 0, 0]

            orbit_radii[orbit_object_name] = system.get_orbit_object_distance(orbit_object_name)

    return positions, velocities, angular_velocities, orbit_radii

def run_simulation(system, sim_duration = 2, timestep = 0.00273973*7):
    """
    Function runs orbital simulation. Generates x, y, z, position and velocity vectors, time vector.

    Args: 
        system: Orbital System representing the system orbital system to simulate.
        sim_duration: Float representing length of simulation in years. 
        timestep: Float representing length of simulation timestep in years.
    
    Returns:
        positions: Dictionary holding x, y, z positions for each orbiting object within simulated system.
        time: Numpy array (vector) holding a timestep-ed time vector in years.

    """
    time = np.linspace(0, sim_duration, round(sim_duration/timestep)) # time vector in years
    num_steps = len(time)
    positions, velocities, angular_velocities, orbit_radii = establish_simulation(system, system.orbiting_objects, time) 
    # now we have a position, velocity dictionary for all orbiting objects with initial position conditions defined, have a time vector

    # looping through time
    for i in range(1, num_steps):
        for orbit_object in positions.keys():
            positions[orbit_object][i, 0] = orbit_radii[orbit_object]*math.cos(angular_velocities[orbit_object]*time[i])
            positions[orbit_object][i, 1] = orbit_radii[orbit_object]*math.sin(angular_velocities[orbit_object]*time[i]) 
    
    return positions, time
