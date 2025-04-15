from orbital_system_sim import SpaceObject, Planet, Satellite, Star, OrbitalSystem, PlanetaryOrbitalSystem, StellarOrbitalSystem
import pytest

def test_orb_sys_oneplanet_oneplanet():
    """
    Check that valid orbital system created with one central planet, one planet orbiting
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Earth"

def test_orb_sys_oneplanet_onesatellite():
    """
    Check that valid orbital system created with one central planet, one satellite orbiting
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Deimos"

def test_orb_sys_oneplanet_onestar():
    """
    Check that orbital system NOT created with one central planet, one star orbiting
    """
    # Define objects
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    system = OrbitalSystem("Test system", central_object)
    # Try the illegal thing
    with pytest.raises(TypeError, match="A star cannot orbit a planet."):
        system.add_orbiting_object(orbiting_object)

def test_orb_sys_onesatellite_onesatellite():
    """
    Check that valid orbital system created with one central satellite, one satellite orbiting
    """
    central_object = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    orbiting_object = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Deimos"
    

def test_orb_sys_onesatellite_onestar():
    """
    Check that orbital system NOT created with one central satellite, one star orbiting
    """
    # Define objects
    central_object = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    orbiting_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    system = OrbitalSystem("Test system", central_object)
    # Try the illegal thing
    with pytest.raises(TypeError, match="A star cannot orbit a satellite."):
        system.add_orbiting_object(orbiting_object)

def test_orb_sys_onesatellite_oneplanet():
    """
    Check that orbital system NOT created with one central satellite, one planet orbiting
    """
    # Define objects
    central_object = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    orbiting_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    system = OrbitalSystem("Test system", central_object)
    # Try the illegal thing
    with pytest.raises(TypeError, match="A planet cannot orbit a satellite."):
        system.add_orbiting_object(orbiting_object)

def test_orb_sys_onestar_onestar():
    """
    Check that valid orbital system created with one central star, one star orbiting
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Star("Proxima Centuari", 107292.36, 1.989e30*0.1221, 0, 0, 0, 3.828e26*0.0017, "Red Dwarf")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Proxima Centuari"

def test_orb_sys_onestar_oneplanet():
    """
    Check that valid orbital system created with one central star, one planet orbiting
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Mars"

def test_orb_sys_onestar_onesatellite():
    """
    Check that valid orbital system created with one central star, one satellite orbiting
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Phobos"

def test_invalid_distance_from_center(): #this test is expected to pass under the failure condition
    """
    Check (when adding object) that orbital object distance_from_center values do not place object within radius of central object
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 0.0004, "rocky")
    system = OrbitalSystem("Test system", central_object)
    with pytest.raises(ValueError, match="The distance between the orbiting object and the central object must be greater than the radius of the central object."):
        system.add_orbiting_object(orbiting_object)

def test_valid_distance_from_center(): #this test is expected to pass under the success condition
    """
    Check (when adding object) that orbital object distance_from_center values do not place object within radius of central object
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)
    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Earth"

def test_valid_period():
    """
    Check that the period of objects around central objects is valid
    """
    pass

def test_space_object_get_name():
    """
    Check get_name function for SpaceObject class
    """
    pass

def test_orbital_system_orbiting_objects_list():
    """
    Check orbiting_objects_list function for OrbitalSystem class
    """
    pass

def test_orbital_system_add_orbiting_object():
    """
    Check add_orbiting_objects function for OrbitalSystem class
    """
    pass

def test_orbital_system_get_orbital_period():
    """
    Check get_orbital_period function for OrbitalSystem class
    """
    pass

def test_orbital_system_get_orbit_object_distance():
    """
    Check get_orbit_object_distance function for OrbitalSystem class
    """
    pass

def test_orbital_system_get_central_object():
    """
    Check get_central_object function for OrbitalSystem class
    """
    pass

def test_planetary_orbital_system_add_orbiting_object():
    """
    Check add_orbiting_object function for PlanetaryOrbitalSystem class
    """
    pass

def test_planetary_orbital_system_orbiting_objects_list():
    """
    Check orbiting_objects_list for PlanetaryOrbitalSystem class
    """
    pass

def test_stellar_orbital_system_init():
    """
    Check StellarOrbitalSystem initialization (central object is a Star)
    """
    pass