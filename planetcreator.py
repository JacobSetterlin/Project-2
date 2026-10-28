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
        name = input('Enter the name of your planet or enter.')
        description = input('Type out everything you want to remember about the planet. ')

        user_input = input(f'Are you sure to want to create the planet called {name}? y/n: ')

        if user_input == 'y':
            CustomPlanet.created_planets[name] = CustomPlanet(name, description)
            print("Your planet has been created.")

        else:
            print("Your planet has not be created")