# Creates orbit objects, runs orbital simulation, in OrbitalSimulation class how to print the name of the stellar system from stellar class when representing

# TO-DO:
# unit check luminosity in star class, planet moons are satellite objects 

class SpaceObject:
    """
    Represents an orbital object in space. Has subclasses Star, Planet, Satellite.

    Attributes:
        name: A string representing the name of the space object. 
        radius: A float representing the radius of the object (all abstracted as spheres) in km.
        mass: A float representing the mass of the object in kg.
        start_x: A float representing the starting x position of space object in AU. 
        start_y: A float representing the starting y position of space object in AU. 
        start_z: A float representing the starting z position of space object in AU. 
    """

    def __init__(self, name, radius, mass, start_x, start_y, start_z):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.start_x = start_x
        self.start_y = start_y
        self.start_z = start_z

    def __repr__(self):
        return f"SPACE OBJECT | Name: {self.name}, radius: {self.radius} km, mass: {self.mass} kg, x start: {self.start_x}, y start: {self.start_y}, z start: {self.start_z}"
    
class OrbitingObject(SpaceObject):
    """
    Represents all orbiting objects.

    Attributes:
        distance_from_center = Float representing semi-major axis in AU.
    """
    
    def __init__(self, name, radius, mass, start_x, start_y, start_z, distance_from_center, ):
        super().__init__(name, radius, mass, start_x, start_y, start_z)
        self.distance_from_center = distance_from_center
    
    def __repr__(self):
        return f"{super().__repr__()}, semi-major axis: {self.distance_from_center} AU"

class Star(SpaceObject):
    """
    Representation of a star (central point of orbit).

    Attributes:
        luminosity: An int representing the luminosity of the star. Total amount of energy radiated per unit time. 
    """

    def __init__(self, luminosity, spectral_type):
        self.luminosity = luminosity
        self.spectral_type = spectral_type

    def __repr__(self):
        return f"{super().__repr__()}, luminosity: {self.distance_from_center} AU, spectral type: {spectral_type}"


class Planet(OrbitingObject):
    """
    Representation of a planet (orbits center)

    Attributes:
        planet_type: A string representing the type of planet (gaseous or rocky).
        moons: An int representing the number of moons the planet has. 
    """

    def __init__(self, planet_type, moons):
        self.planet_type = planet_type
        self.moons = moons

    def __repr__(self):
        return f"{super().__repr__()}, planet type: {self.planet_type}, number of moons: {self.moons}"

class Satellite(OrbitingObject): 
    """
    Representation of a space satellite. 

    Attributes:
        lifetime: A float representing the expected lifetime of satellite in years.
        material: A string representing the primary material of the satellite.
    """

    def __init__(self, name, lifetime, material):
        self.name = name
        self.lifetime = lifetime
        self.material = material

    def __repr__(self):
        return f"{super().__repr__()}, lifetime: {self.lifetime} years, material: {self.material}"

class StellarOrbitalSystem:
    """
    Composition class, represents orbital system.

    Attributes:
        name: A string representing the name of the orbital sytem.
        star: A Star object representing the center of the orbit.
    """
    def __init__(self, name, star):
        self.name = name
        self.star = star
    
    def __repr__(self):
        return f"System name: {self.name}, Central Star: {self.star}"

    # calculate period between star and orbiting objects
    # error if there are not oribiting objects 


class OrbitSimulation:
    """
    Runs the orbit simulation from orbital system instances.

    Attributes:
        sim_duration: Float representing length of simulation in years. 
        timestep: Float representing length of simulation timestep in years.

    """
    
    def __init__(self, sim_duration, timestep, system):
        self.sim_duration = sim_duration
        self.timestep = timestep
        self.system = system
    
    def __repr__(self):
        return f"Sim duration: {self.sim_duration} years, Timestep: {self.timestep} years"