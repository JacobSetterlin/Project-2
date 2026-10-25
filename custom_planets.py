"""
custom_planets
Used to hold the custom_planets class

Jacob Setterlin
Last updated on 10/25/2026 
"""
from pathlib import Path

class CustomPlanet:
    """Used to create custom planets for the user."""
    def __init__(self, name, description_path: Path):
        """
        name: the users name for the planet.
        
        description_path: the file path to the description of the planet,
        which should always be found in the planet_descriptions folder.
        """
        self.name = name
        self.description_path = description_path