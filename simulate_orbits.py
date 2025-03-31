# File holds simulation function
import numpy as np

def run_simulation(system, sim_duration = 2, timestep = 0.00273973*7):
    """
    Function runs orbital simulation. Generates x, y, z, position and velocity vectors, time vector.

    Args: 
        system: Orbital System representing the system orbital system to simulate.
        sim_duration: Float representing length of simulation in years. 
        timestep: Float representing length of simulation timestep in years.
    
    Outputs:

    """
    time = np.linspace(0, sim_duration, round(sim_duration/timestep)) # time vector in years
    num_steps = len(time)

    # Dictionaries to store positions and velocities
    positions = {}
    velocities = {}

    for orbit_object_name, orbit_object in system.orbiting_objects.items():
        # create an array of shape
        positions[orbit_object_name] = np.zeros((num_steps, 3))
        velocities[orbit_object_name] = np.zeros((num_steps, 3))

        positions[orbit_object_name][0] = [orbit_object.start_x, orbit_object.start_y, orbit_object.start_z]
        velocities[orbit_object_name][0] = [0, 0, 0]

    return positions, velocities, time
