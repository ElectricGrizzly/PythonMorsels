# Problem Statement
This exercise includes **3 bonuses** and **10 hints** (hover over the hint links before clicking on them).

I'd like you to write a class representing a 3-dimensional point.

The Point class must accept 3 values on initialization (x, y, and z) and have _x_, _y_, and _z_ attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

Example usage:
```
>>> p1 = Point(1, 2, 3)
>>> p1
Point(x=1, y=2, z=3)
>>> p2 = Point(1, 2, 3)
>>> p1 == p2
True
>>> p2.x = 4
>>> p1 == p2
False
>>> p2
Point(x=4, y=2, z=3)
```
If you finish the base exercise quickly, consider working through a bonus or two.
## Bonus 1
For the first bonus, I'd like you to allow Point objects to be added and subtracted from each other.
```
>>> p1 = Point(1, 2, 3)
>>> p2 = Point(4, 5, 6)
>>> p1 + p2
Point(x=5, y=7, z=9)
>>> p3 = p2 - p1
>>> p3
Point(x=3, y=3, z=3)
```
## Bonus 2
For the second bonus, I'd like you to allow Point objects to be scaled up and down by numbers.
```
>>> p1 = Point(1, 2, 3)
>>> p2 = p1 * 2
>>> p2
Point(x=2, y=4, z=6)
```
## Bonus 3
```
>>> p1 = Point(1, 2, 3)
>>> x, y, z = p1
>>> (x, y, z)
(1, 2, 3)
```
## Hints
Hints for **when you get stuck** (hover over links to see what they're about):
- [What is a class?](https://www.pythonmorsels.com/topics/what-is-a-class/ "Short screencast explaining classes, attributes, and methods")
- [Customizing the string representation of your class](https://www.pythonmorsels.com/topics/customizing-string-representation-your-objects/ "You need to write a __repr__ method")
- [How operator overloading works in Python](https://www.pythonmorsels.com/topics/what-are-dunder-methods/ "==, +, and many other operators are powered by dunder methods in Python")
- [Comparing equality of tuples](https://treyhunner.com/2019/03/python-deep-comparisons-and-code-readability/#Deep_equality "Deep comparisons can make for slightly nicer equality checks")
- [Bonus 1: Adding class instances](https://thepythonguru.com/python-operator-overloading/ "You can make objects addable by making a __add__ method")
- [Bonus 2: Allowing objects to be multiplied by numbers](http://www.openbookproject.net/thinkcs/python/english2e/ch15.html#operator-overloading "You'll need to make both __mul__ and __rmul__ methods")
- [Bonus 2: Handling operations with arbitrary types](https://docs.python.org/3/library/constants.html#NotImplemented "When a binary operation on a given type isn't supported, NotImplemented should be returned")
- [Bonus 2: A short Twitter thread on that topic](https://twitter.com/treyhunner/status/1214636577441427457 "NotImplemented allows your object to tell Python that it should delegate to the right-hand-side object instead")
- [Bonus 3: Multiple assignment and tuple unpacking](https://www.pythonmorsels.com/topics/tuple-unpacking/ "Unpacking a sequence and assigning multiple variables with a single line of code")
- [Bonus 3: Creating objects that work with multiple assignment](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/#Generators_can_help_when_making_iterables_too "Multiple assignment only works with iterables")