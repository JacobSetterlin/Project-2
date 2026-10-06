"""
planet
Jacob Setterlin

This File is used to hold the Planet Class.
Last Updated 10/6/2026
"""

class Planet:
    """This Class is used to create planet objects."""

    def __init__(self, name: str, distance_from_sun: float, atmosphere: str):
        """
        Used to create Planet objects.
        Name: The name of the planet.
        distance_from_sun: The distance of the planet from our sun in astronomical units.
        Atmospshere: The most common gas in the planets atmosphere.
        """

        self.name = name
        self.distance_from_sun = distance_from_sun
        self.atmosphere = atmosphere