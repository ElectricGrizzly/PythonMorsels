# Problem Statement
This exercise includes **2 bonuses** and **6 hints** (hover over the hint links before clicking on them).

I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:
```
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
```
Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

There are two bonuses for this exercise.
## Bonus 1
For the first bonus, modify your add function to accept and "add" any number of lists-of-lists.
```
>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
```
## Bonus 2
For the second bonus, make sure your add function raises a _ValueError_ if the given lists-of-lists aren't all the same shape.
```
>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
```
## Hints
Hints for **when you get stuck** (hover over links to see what they're about):
- [Looping with indexes](https://www.pythonmorsels.com/topics/looping-with-indexes/ "The built-in enumerate function can help you loop with indexes")
- [Looping over multiple lists at the same time](https://www.pythonmorsels.com/topics/looping-over-multiple-iterables/ "The built-in zip function can be helpful for looping over multiple iterables at once")
- [Multiple assignment might come in handy](https://www.pythonmorsels.com/topics/tuple-unpacking/ "Multiple assignment can help improve code readability, especially in loops")
- [A special syntax for creating new lists from old lists](https://www.pythonmorsels.com/topics/what-are-list-comprehensions/ "List comprehensions are a special purpose tool for creating a new list from an old list")
- [Bonus 1: Accepting any number of arguments to a function](https://www.pythonmorsels.com/topics/accepting-any-number-arguments-function/ "The * operator can be used for writing a function that accepts any number of positional arguments")
- [Bonus 2: Raising an exception in Python](https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python "Examples of how to raise an exception manually in Python")