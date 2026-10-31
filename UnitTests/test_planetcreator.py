from planetcreator import PlanetCreator
import unittest.mock as mock

def test_create_planet():
    planet_creator = PlanetCreator()
    planet_creator.created_planets = {}
    name = 'name'
    desc = 'description'

    with mock.patch("builtins.input", side_effect = [name, desc, 'y']):
        planet_creator.create_planet()

    assert planet_creator.created_planets == {name: desc}