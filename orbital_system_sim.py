# Creates orbit objects, runs orbital simulation

import math
GRAVITATIONAL_CONSTANT = 6.67408*10**(-11)/149597870691**3 #m^3/kgs^2 -> AU/kgs^2 


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
    
    def __init__(self, name, radius, mass, start_x, start_y, start_z, distance_from_center):
        super().__init__(name, radius, mass, start_x, start_y, start_z)
        self.distance_from_center = distance_from_center
    
    def __repr__(self):
        return f"{super().__repr__()}, semi-major axis: {self.distance_from_center} AU"


class Star(SpaceObject):
    """
    Representation of a star (central point of orbit).

    Attributes:
        luminosity: An int representing the luminosity of the star (Watts). Total amount of energy radiated per unit time. 
    """

    def __init__(self, name, radius, mass, start_x, start_y, start_z, luminosity, spectral_type):
        super().__init__(name, radius, mass, start_x, start_y, start_z)
        self.luminosity = luminosity
        self.spectral_type = spectral_type

    def __repr__(self):
        return f"{super().__repr__()}, luminosity: {self.luminosity} Watts, spectral type: {self.spectral_type}"


class Planet(OrbitingObject):
    """
    Representation of a planet (orbits center)

    Attributes:
        planet_type: A string representing the type of planet (gaseous or rocky).
    """

    def __init__(self, name, radius, mass, start_x, start_y, start_z, distance_from_center, planet_type):
        super().__init__(name, radius, mass, start_x, start_y, start_z, distance_from_center)
        self.planet_type = planet_type

    def __repr__(self):
        return f"{super().__repr__()}, planet type: {self.planet_type}"


class Satellite(OrbitingObject): 
    """
    Representation of a space satellite. 

    Attributes:
        lifetime: A float representing the expected lifetime of satellite in years.
        material: A string representing the primary material of the satellite.
    """

    def __init__(self, name, radius, mass, start_x, start_y, start_z, distance_from_center, lifetime, material):
        super().__init__(name, radius, mass, start_x, start_y, start_z, distance_from_center)
        self.lifetime = lifetime
        self.material = material

    def __repr__(self):
        return f"{super().__repr__()}, lifetime: {self.lifetime} years, material: {self.material}"
    

class OrbitalSystem:
    """
    Parent composition class, represents all orbital systems, with a central object and orbiting objects.
    
    Attributes:
        name: A string representing the name of the orbital sytem.
        central_object: A central object representing the center of the orbit.
        orbit_objects: A dictionary of orbiting objects / period within system - names are keys.
    """
    def __init__(self, name, central_object):
        """Initialize the system with a single central object and an empty dictionary of orbiting objects."""
        self.name = name
        self.central_object = central_object
        self.orbiting_objects = {} 
    
    def __repr__(self):
        return f"System name: {self.name}, Central Object: {self.central_object}, Number of orbiting objects: {len(self.orbiting_objects)}"
    
    def orbiting_objects_list(self):
        """Returns string of all orbiting objects in orbital system."""
        temp = []
        for name in self.orbiting_objects.keys():
            temp.append(name)
        return f"Orbiting Objects in {self.name}: {', '.join(temp)}"
    
    def add_orbiting_object(self, object):
        """Allows user to add orbiting objects to system"""
        self.orbiting_objects[object.name] = object
    
    def get_orbital_period(self, object_name):
        """Returns the orbital period of an orbiting object in Earth years."""
        object = self.orbiting_objects.get(object_name)
        if isinstance(object, OrbitingObject):
            period = math.sqrt( (object.distance_from_center**3*4*math.pi**2)/(GRAVITATIONAL_CONSTANT*(object.mass + self.central_object.mass)) ) /31536000
            return period
        elif isinstance(object, OrbitalSystem):
            # take the period from the central object 
            period = math.sqrt( (object.central_object.distance_from_center**3*4*math.pi**2)/(GRAVITATIONAL_CONSTANT*(object.central_object.mass + self.central_object.mass)) ) /31536000
            return period
        else:
            raise ValueError(f"Object '{object_name}' not found in system.")
        
    def get_orbit_object_distance(self, object_name):
        """Returns the distance from the central object to the orbital object in AU."""
        object = self.orbiting_objects.get(object_name)
        if len(self.orbiting_objects) == 0:
            return "There are no orbiting objects in the system."
        elif isinstance(object, OrbitingObject):
            return object.distance_from_center
        elif isinstance(object, PlanetaryOrbitalSystem):
            return object.central_object.distance_from_center

        else:
            raise ValueError(f"Object '{object_name}' not found in system.")
    

class PlanetaryOrbitalSystem(OrbitalSystem):
    """
    Compsition class, represents orbital systems around planets.

    Attributes:
        planet: A Planet object representing the planet at the center of the orbital system
        moons: A dictionary representing the moons (satellites) of the planet, key is name, value is period.
    """
    def __init__(self, name, planet):
        """Initialize the system with a single central star and an empty dictionary of orbiting objects."""
        if not isinstance(planet, Planet):
            raise TypeError("The central object must be a Planet.")
        super().__init__(name, planet)
        self.moons = {} 
        self.start_x = planet.start_x
        self.start_y = planet.start_y
        self.start_z = planet.start_z

    def __repr__(self):
        return f"System name: {self.name}, Central Object: {self.central_object}, Number of orbiting objects: {len(self.moons)}"
    

    def add_moon(self, object):
        """Allows user to add satellites to planet"""
        if not isinstance(object, Satellite):
            raise TypeError("The orbiting object must be a Satellite.")
        self.moons[object.name] = object

    def moon_list(self):
        """Returns string of all moons around planet."""
        temp = []
        for name in self.moons.keys():
            temp.append(name)
        return f"Moons in {self.name}: {', '.join(temp)}"
    

class StellarOrbitalSystem(OrbitalSystem):
    """
    Composition class, represents orbital system around stars.

    Attributes:
        name: A string representing the name of the orbital sytem.
        star: A Star object representing the center of the orbit.
        orbit_objects: A dictionary of orbiting objects / period within system - names are keys.
    """
    def __init__(self, name, star):
        """Initialize the system with a single central star and an empty dictionary of orbiting objects."""
        if not isinstance(star, Star):
            raise TypeError("The central object must be a Star.")
        super().__init__(name, star)