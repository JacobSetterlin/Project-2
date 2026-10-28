"""
Planet Information
Jacob Setterlin

This program is used to find provide the user with the information of a planet 
they want to know about.

All information comes from NASA unless stated otherwise.

Last Updated: 10/25/2026"""

from planet import Planet
from pathlib import Path

def line_break():
    """Used to seperate different messages and user input in the console."""
    print("--------------------")

def check_for_quitting():
    """Checks if the user has decided to quit the program."""
    if user_input == "q":
            quit()

native_folder = 'nativeplanetsdescriptions'

native_planet = {"mercury": Planet("Mercury", 0.4, "sodium", Path.cwd() / native_folder / 'mercury.txt'),
                "venus": Planet("Venus", 0.72, "carbon dioxide", Path.cwd() / native_folder / 'venus.txt'),
                "earth": Planet("Earth", 1, "oxygen", Path.cwd() / native_folder / 'earth.txt'),
                "mars": Planet("Mars", 1.5, "carbon dioxide", Path.cwd() / native_folder / 'mars.txt'),
                "jupiter": Planet("Jupiter", 5.2, "ammonia ice", Path.cwd() / native_folder / 'jupiter.txt'),
                "saturn": Planet("Saturn", 9.5, "hydrogen", Path.cwd() / native_folder / 'saturn.txt'),
                "uranus": Planet("Uranus", 19, "hydrogen", Path.cwd() / native_folder / 'uranus.txt'),
                "neptune": Planet("Neptune", 30, "hydrogen", Path.cwd() / native_folder / 'neptune.txt')}

print("All information is retrieved from NASA unless stated otherwise.")
while True:
    print("Enter the name of the planet you want to learn about, or press q to quit.")
    print("Available Planets:")
    
    for planet in native_planet:
        print(planet)
    line_break()

    user_input = input().lower()
    line_break()

    check_for_quitting()

    print(f'{native_planet[user_input].name}:')
    print(f'{native_planet[user_input].distance_from_sun} astronomical units from our sun.')
    print(f'The atmosphere of {native_planet[user_input].name} is made mostly of {native_planet[user_input].atmosphere}')

    with open(native_planet[user_input].desc_path, 'r') as file:
        print(file.read())
  
    line_break()

    user_input = input('Press enter to continue, or enter q to quit.').lower()

    check_for_quitting()
    
    line_break()