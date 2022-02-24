'''
Provides a circle object with radius, diameter, and area ttributes.

Written for Python Morsels Exercise/Assignment #2 "circle"

Classes:

    Circle
    - Provides circle representation
'''

from math import pi

class Circle:
    '''
    A class to represent a circle.

    ...

    Attributes
    ----------
    radius: int|float
        radius of the circle
    diameter: int|float
        diameter of the circle
    area: int|float
        area of the circle
    '''
    def __init__(self, radius: int|float = 1) -> None:
        '''
        Constructs all the necessary attributes for the circle object.

        Parameters
        ----------
            radius: int|float
                radius of the circle
        '''
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius
    
    def __repr__(self) -> str:
        return f'Circle({self.radius})'
    
    @property
    def radius(self) -> int|float:
        return self._radius
    
    @radius.setter
    def radius(self, radius: int|float = 1) -> None:
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius
    
    @property
    def diameter(self) -> int|float:
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, diameter: int|float = 2) -> None:
        if diameter < 0:
            raise ValueError('Diameter cannot be negative')
        self._radius = diameter / 2
    
    @property
    def area(self) -> float:
        return pi * self.radius * self.radius