# Creates orbit objects, runs orbital simulation

class SpaceObject:
    """
    Represents an orbital object in space. Has subclasses Star, Planet, Satellite.

    Attributes:
        radius: A float representing the radius of the object (all abstracted as spheres).
        mass: A float representing the mass of the object. 
    """

    def __innit__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    

class Star(SpaceObject):
    """
    Representation of a star (central point of orbit).
    """


class Planet(SpaceObject):
    """
    Representation of a planet (orbits center)
    """

class Satellite(SpaceObject): 
    """
    Representation of a space satellite. 
    """

class StellarOrbitalSystem:
    """
    Composition class, represents orbital system.

    Attributes:
        star: A Star object representing the center of the orbit.
    """
    def __innit__(self, star):
        self.star = star