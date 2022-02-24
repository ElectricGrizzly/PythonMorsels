# Problem Statement
This exercise includes **3 bonuses** and **7 hints** (hover over the hint links before clicking on them).

I want you to make a class that represents a circle.

The circle should have a _radius_, a _diameter_, and an _area_. It should also have a nice string representation.

For example:
```
>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
```
Additionally the radius should default to 1 if no radius is specified when you create your circle:
```
>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2
```
There are three bonuses for this exercise.
## Bonus 1
For the first bonus, make sure when the _radius_ of your class changes that the _diameter_ and _area_ both change as well:
```
>>> c = Circle(2)
>>> c.radius = 1
>>> c.diameter
2
>>> c.area
3.141592653589793
>>> c
Circle(1)
```
If you get stuck on this bonus, make sure to check the hints.
## Bonus 2
For the second bonus, make sure you can set the _diameter_ attribute in your class and the _radius_ will update accordingly. Also make sure also that you cannot set the _area_ (setting area should raise an _AttributeError_):
```
>>> c = Circle(1)
>>> c.diameter = 4
>>> c.radius
2.0
>>> c.area = 45.678
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 16, in radius
AttributeError: can't set attribute
```
## Bonus 3
For the third bonus, make sure your radius cannot be set to a negative number. You should raise a _ValueError_ exception with the error message "Radius cannot be negative".
```
>>> c = Circle(5)
>>> c.radius = 3
>>> c.radius = -2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
>>> c = Circle (-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "circle.py", line 27, in radius
    raise ValueError("Radius cannot be negative")
ValueError: Radius cannot be negative
```
This means that _diameter_ cannot be negative either (and setting _diameter_ to a negative number should also raise a _ValueError_).
## Hints
Here are some hints you can use **when you get stuck** (hover over links to see what they're about):
- [What is a class?](https://www.pythonmorsels.com/topics/what-is-a-class/ "Short screencast explaining classes, attributes, and methods")
- [Computing the area of a circle](https://en.wikipedia.org/wiki/Area_of_a_circle "You probably don't need geometry every day, right?")
- [Customizing the string representation of your class](https://www.pythonmorsels.com/topics/customizing-string-representation-your-objects/ "You need to write a __repr__ method")
- [Where to find math utilities](https://docs.python.org/3/library/math.html#math.pi "You'll want to use pi from the math library")
- [Bonus 1: Making an auto-updating attribute](https://www.pythonmorsels.com/topics/making-auto-updating-attribute/ "Properties are the way we make auto-updating attributes on classes")
- [Bonus 2: Customizing what happens when you set an attribute](https://www.pythonmorsels.com/topics/customizing-what-happens-when-you-assign-attribute/ "Properties can have a setter")
- [Bonus 3: Raising exceptions](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python "Manually raising exceptions")