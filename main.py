"""
Planet Information
Jacob Setterlin

This program is used to find provide the user with the information of a planet 
they want to know about.

All information comes from NASA unless stated otherwise.

Last Updated: 9/27/2026"""

from planet import Planet

def line_break():
    """Used to seperate different messages and user input in the console."""
    print("--------------------")

available_planets = {"mercury": Planet("Mercury", 0.4, "sodium"),
                     "venus": Planet("Venus", 0.72, "carbon dioxide"),
                     "earth": Planet("Earth", 1, "oxygen"),
                     "mars": Planet("Mars", 1.5, "carbon dioxide"),
                     "jupiter": Planet("Jupiter", 5.2, "ammonia ice"),
                     "saturn": Planet("Saturn", 9.5, "hydrogen"),
                     "uranus": Planet("Uranus", 19, "hydrogen"),
                     "neptune": Planet("Neptune", 30, "hydrogen")}

print("All information is retrieved from NASA unless stated otherwise.")
while True:
    print("Enter the name of the planet you want to learn about, or press q to quit.")
    print("Available Planets:")
    for planet in available_planets:
        print(planet)
    line_break()

    user_input = input().lower()
    line_break()

    if user_input == "q":
        quit()

    print(available_planets[user_input].name)
    print(available_planets[user_input].distance_from_sun)
    print(available_planets[user_input].atmosphere)
    
    line_break()