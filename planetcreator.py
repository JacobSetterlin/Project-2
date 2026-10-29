"""
planetscreator
Jacob Setterlin

This file is used to store the PlanetCreator class.
"""

class PlanetCreator():
    """Used to create custom planets for the user."""

    created_planets = {}

    def create_planet(self):
        """Used to create planets for the user."""
        name = input('Enter the name of your planet. ').lower()
        description = input('Type out everything you want to remember about the planet. ')

        user_input = input(f'Are you sure to want to create the planet called {name}? y/n: ')

        if user_input == 'y':
            self.created_planets[name] = description
            print("Your planet has been created.")

        else:
            print("Your planet has not be created")