"""
Planet Information
Jacob Setterlin

This program is used to find provide the user with the information of a planet 
they want to know about.

All information comes from NASA unless stated otherwise.

Last Updated: 10/29/2026"""

from planet import Planet
from pathlib import Path
from planetcreator import PlanetCreator
import json

class Main():
    """Used to hold the main logic of the program."""
    
    native_folder = 'nativeplanetsdescriptions'
    
    native_planet = {"mercury": Planet("Mercury", 0.4, "sodium", Path.cwd() / native_folder / 'mercury.txt'),
                    "venus": Planet("Venus", 0.72, "carbon dioxide", Path.cwd() / native_folder / 'venus.txt'),
                    "earth": Planet("Earth", 1, "oxygen", Path.cwd() / native_folder / 'earth.txt'),
                    "mars": Planet("Mars", 1.5, "carbon dioxide", Path.cwd() / native_folder / 'mars.txt'),
                    "jupiter": Planet("Jupiter", 5.2, "ammonia ice", Path.cwd() / native_folder / 'jupiter.txt'),
                    "saturn": Planet("Saturn", 9.5, "hydrogen", Path.cwd() / native_folder / 'saturn.txt'),
                    "uranus": Planet("Uranus", 19, "hydrogen", Path.cwd() / native_folder / 'uranus.txt'),
                    "neptune": Planet("Neptune", 30, "hydrogen", Path.cwd() / native_folder / 'neptune.txt')}

    planet_creator = PlanetCreator()

    created_planets = {}

    def main(self):
            """Used to hold the main logic the program."""
            
            self.created_planets = self._gather_save_data()
            print("All information is retrieved from NASA unless stated otherwise.")
            
            while True:
                print("Enter the name of the planet you want to learn about, enter c to create a planet, or enter q to quit.")
                print("Available Planets:")
                
                self._display_planets()
                self._line_break()
    
                user_input = input().lower()
                self._line_break()
    
                self._handle_input(user_input)
            
                self._line_break()
    
                user_input = input('Press enter to continue, or enter q to quit. ').lower()
                self._handle_input(user_input)
                
                self._line_break()

    def _gather_save_data(self):
            with open(Path.cwd() / 'savestates' / 'userplanets.json', 'r') as file:
                return json.load(file)

    def _line_break(self):
        """Used to seperate different messages and user input in the console."""
        print("--------------------")

    def _display_planets(self):
        """Used to display the planets the user can view information on."""
        for planet in self.native_planet:
            print(planet)
        for planet in self.created_planets:
            print(planet)

    def _display_native_planet_info(self, user_input):
        """Used to display information about built in planets."""
        print(f'{self.native_planet[user_input].name}:')
        print(f'{self.native_planet[user_input].distance_from_sun} astronomical units from our sun.')
        print(f'The atmosphere of {self.native_planet[user_input].name} is made mostly of {self.native_planet[user_input].atmosphere}')

        with open(self.native_planet[user_input].desc_path, 'r') as file:
            print(file.read())

    def _display_custom_planet(self, user_input):
        """Used to display information about user made planets"""
        print(f'{user_input}: ')
        print(self.created_planets[user_input])

    def _handle_input(self, user_input):
        """Handles logic based on the users choice of input."""
        if user_input in self.native_planet:
            self._display_native_planet_info(user_input)

        elif user_input in self.created_planets:
            self._display_custom_planet(user_input)

        elif user_input == 'c':
            self.planet_creator.create_planet()
            
            with open(Path.cwd() / 'savestates' / 'userplanets.json', 'w') as file:
                json.dump(PlanetCreator.created_planets, file)
            
            self.created_planets = self._gather_save_data()

        elif user_input == 'q':
            quit()

        else:
            print('Command not recognized.')

if __name__ == '__main__':
    main_program = Main()
    main_program.main()