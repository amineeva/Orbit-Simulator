from orbital_system_sim import SpaceObject, Planet, Satellite, Star, OrbitalSystem, PlanetaryOrbitalSystem, StellarOrbitalSystem
import pytest
from unittest.mock import patch

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
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Earth"

def test_invalid_distance_from_center(): #this test is expected to pass under the failure condition
    """
    Check (when adding object) that orbital object distance_from_center values do not place object within radius of central object
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
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
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)
    assert system.get_orbital_period("Earth") == 1.0005703560107866

def test_orbital_system_orbiting_objects_list_no_objects():
    """
    Check orbiting_objects_list function for OrbitalSystem class with 0 objects
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    system = OrbitalSystem("Test system", central_object)
    assert system.orbiting_objects_list() == "There are no orbiting objects in the system."

def test_orbital_system_orbiting_objects_list_some_objects():
    """
    Check orbiting_objects_list function for OrbitalSystem class with 2 OrbitObjects
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    orbiting_object_2 = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    system.add_orbiting_object(orbiting_object_2)
    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Earth, Mars"

def test_orbital_system_orbiting_objects_list_orbital_systems():
    """
    Check orbiting_objects_list function for OrbitalSystem class with combined OrbitObject and OrbitalSystem instances
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    orbiting_object_2 = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid") # creating Martian planet moons as satellite instances
    deimos_moon = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    mars_system = PlanetaryOrbitalSystem("Mars system", mars_planet) # creating Mars orbit system 
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    system.add_orbiting_object(orbiting_object_2)
    system.add_orbiting_object(mars_system)
    assert system.orbiting_objects_list() == "Orbiting Objects in Test system: Earth, Mars, Mars system"

def test_orbital_system_get_orbital_period():
    """
    Check get_orbital_period function for OrbitalSystem class
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    assert system.get_orbital_period("Earth") == 1.0005703560107866

def test_orbital_system_get_orbital_period_invalid():
    """
    Check get_orbital_period function for OrbitalSystem class - getting period for object not in orbiting list
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    with pytest.raises(ValueError, match="Object Mars not found in system."):
        system.get_orbital_period("Mars")

def test_orbital_system_get_orbital_period_no_orbiting_object():
    """
    Check get_orbital_period function for OrbitalSystem class - no objects in orbiting list 
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    system = OrbitalSystem("Test system", central_object)
    assert system.get_orbital_period("Mars") == "There are no orbiting objects in the system."

def test_orbital_system_get_orbit_object_distance_correct():
    """
    Check get_orbit_object_distance function for OrbitalSystem class, getting distance for object not in the orbiting list
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    assert system.get_orbit_object_distance("Earth") == 1.0

def test_orbital_system_get_orbit_object_distance_invalid():
    """
    Check get_orbit_object_distance function for OrbitalSystem class, from an orbiting object
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    with pytest.raises(ValueError, match="Object Mars not found in system."):
        system.get_orbit_object_distance("Mars")

def test_orbital_system_get_orbit_object_distance_no_orbiting_objects():
    """
    Check get_orbit_object_distance function for OrbitalSystem class - no orbiting objects in system
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    system = OrbitalSystem("Test system", central_object)
    assert system.get_orbit_object_distance("Mars") == "There are no orbiting objects in the system."

def test_orbital_system_get_orbit_object_distance_system_orbiting():
    """
    Check get_orbit_object_distance function for OrbitalSystem class, system orbiting 
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid") # creating Martian planet moons as satellite instances
    deimos_moon = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    mars_system = PlanetaryOrbitalSystem("Mars system", mars_planet) # creating Mars orbit system 
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(mars_system)
    assert system.get_orbit_object_distance("Mars system") == 1.5

def test_orbital_system_get_orbit_object_distance_system_orbiting_call_planet():
    """
    Check get_orbit_object_distance function for OrbitalSystem class, system orbiting calling the name of an object within orbiting system
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    phobos_moon = Satellite("Phobos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid") # creating Martian planet moons as satellite instances
    deimos_moon = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    mars_system = PlanetaryOrbitalSystem("Mars system", mars_planet) # creating Mars orbit system 
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(mars_system)
    with pytest.raises(ValueError, match="Object Mars not found in system."):
        system.get_orbit_object_distance("Mars")
    
def test_orbital_system_get_central_object_one_planet():
    """
    Check get_central_object function for OrbitalSystem class
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(mars_planet)
    assert system.get_central_object() == system.central_object

def test_orbital_system_get_central_object_no_orbiting_objects():
    """
    Check get_central_object function for OrbitalSystem class, no orbiting objects
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    mars_planet = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    system = OrbitalSystem("Test system", central_object)
    assert system.get_central_object() == system.central_object

def test_planetary_orbital_system_oneplanet_oneplanet():
    """
    Check add_orbiting_object function for PlanetaryOrbitalSystem class, one planet - one planet
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    system = PlanetaryOrbitalSystem("Test system", central_object)
    
    with pytest.raises(TypeError, match="The orbiting object must be a Satellite."):
        system.add_orbiting_object(orbiting_object)

def test_planetary_orbital_system_oneplanet_onestar():
    """
    Check add_orbiting_object function for PlanetaryOrbitalSystem class, one planet - one star
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    system = PlanetaryOrbitalSystem("Test system", central_object)
    
    with pytest.raises(TypeError, match="The orbiting object must be a Satellite."):
        system.add_orbiting_object(orbiting_object)

def test_planetary_orbital_system_oneplanet_onesatellite():
    """
    Check that valid orbital system created with one central planet, one satellite orbiting
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    orbiting_object = Satellite("Deimos", 11, 0, 0, 0, 0, 0.00004011, 100, "asteroid")
    system = PlanetaryOrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object)

    assert system.orbiting_objects_list() == "Moons in Test system: Deimos (4.011e-05 AU)"

def test_stellar_orbital_system_init():
    """
    Check StellarOrbitalSystem initialization (central object is a Star)
    """
    central_object = Planet("Mars", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    
    with pytest.raises(TypeError, match = "The central object must be a Star."):
        StellarOrbitalSystem("Test system", central_object)

def test_add_same_object():
    """
    Check that adding two of the same object asks for user input before adding to list
    """
    central_object = Star("Sun", 695700, 1.989e30, 0, 0, 0, 3.828e26, "O-type")
    orbiting_object_1 = Planet("Earth", 6371, 5.972e24, 0, 0, 0, 1.0, "rocky")
    orbiting_object_2 = Planet("Earth", 3390, 6.4191*10**23, 0, 0, 0, 1.5, "rocky")
    system = OrbitalSystem("Test system", central_object)
    system.add_orbiting_object(orbiting_object_1)
    with patch("builtins.input", return_value="1") as mock_input:
        with patch("builtins.print") as mocked_print:
            result = system.add_orbiting_object(orbiting_object_2)
            mocked_print.assert_called_with("Original replaced")
            mock_input.assert_called_with("You already have an object with the same name in this system. Enter 1 to replace and 2 to cancel.")
    assert system.orbiting_objects[orbiting_object_2.name] == orbiting_object_2