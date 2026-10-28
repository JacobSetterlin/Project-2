"""
planetscreator
Jacob Setterlin

This file is used to store the PlanetCreator class.
"""

from custom_planets import CustomPlanet

class PlanetCreator():
    """Used to create custom planets for the user."""

    def create_planet():
        """Used to create planets for the user."""
        name = input('Enter the name of your planet. ')
        description = input('Type out everything you want to remember about the planet. ')

        CustomPlanet.created_planets[name] = CustomPlanet(name, description)