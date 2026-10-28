"""
custom_planets
Used to hold the custom_planets class

Jacob Setterlin
Last updated on 10/25/2026 
"""
from pathlib import Path

class CustomPlanet:
    """Used to create custom planets for the user."""

    created_planets = {}
    
    def __init__(self, name: str, description: str):
        """
        name: the users name for the planet.
        
        description: The user's descirption of the planet
        """
        self.name = name
        self.description = description