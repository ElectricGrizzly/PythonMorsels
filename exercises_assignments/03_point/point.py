'''
Provides a 3D point object with x, y, and z attributes.

Classes:

    Point
    - Provides a 3D point representation
'''
class Point:
    '''
    A class to represent a 3D point.

    ...

    Attributes
    ----------
    x: int|float
        x value of 3D point
    y: int|float
        y value of 3D point
    z: int|float
        z value of 3D point
    '''
    def __init__(self, x: int|float = 0, y: int|float = 0, z: int|float = 0) -> None:
        '''
        Constructs all the necessary attributes for the point object.

        Parameters
        ----------
            x: int|float
                x value of 3D point
            y: int|float
                y value of 3D point
            z: int|float
                z value of 3D point
        '''
        self._x = x
        self._y = y
        self._z = z

    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            if self.x == __o.x and self.y == __o.y and self.z == __o.z:
                return True
            return False
        else:
            raise NotImplemented
    
    def __add__(self, __o: object) -> object:
        if isinstance(__o, Point):
            return Point(self.x + __o.x, self.y + __o.y, self.z + __o.z)
        else:
            raise NotImplemented
    
    def __sub__(self, __o: object) -> object:
        if isinstance(__o, Point):
            return Point(self.x - __o.x, self.y - __o.y, self.z - __o.z)
        else:
            return NotImplemented
        
    def __mul__(self, value: int|float) -> object:
        if isinstance(value, (int, float)):
            return Point(self.x * value, self.y * value, self.z * value)
        else:
            return NotImplemented
    
    def __rmul__(self, value: int|float) -> object:
        if isinstance(value, (int, float)):
            return Point(self.x * value, self.y * value, self.z * value)
        else:
            return NotImplemented
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
    
    @property
    def x(self) -> int|float:
        return self._x
    
    @x.setter
    def x(self, value: int|float) -> None:
        self._x = value
    
    @property
    def y(self) -> int|float:
        return self._y
    
    @y.setter
    def y(self, value: int|float) -> None:
        self._y = value
    
    @property
    def z(self) -> int|float:
        return self._z
    
    @z.setter
    def z(self, value: int|float) -> None:
        self._z = value