# Problem Statement
This exercise includes **3 bonuses** and **5 hints** (hover over the hint links before clicking on them).

We recommend Intermediate-level users solve the **first 2 bonuses** for this exercise.

In this exercise, we're going to work on flattening iterables. I'd like you to write a function _deep flatten_ that accepts a list of lists (or lists of tuples and lists) and returns a flattened version of that list of lists.

It should work like this:
```
>>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> deep_flatten([[1, [2, 3]], 4, 5])
[1, 2, 3, 4, 5]
```
In the examples above, we're returning a list. Your _deep flatten_ function should return an iterable, not necessarily a list.

Your _deep flatten_ function can assume that no strings will be passed to it. We'll deal with strings later.
## Bonus 1
For the first bonus, I'd like you to make sure your _deep flatten_ function accepts not just lists and tuples, but generators, sets, and other iterable data structures (but don't worry about handling strings yet, as we'll handle them in bonus 3).
```
>>> sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)}))
[1, 2, 3, 4, 5, 6, 7, 8]
```
## Bonus 2
For the second bonus, I'd like you to make _deep flatten_ return an iterator that loops over input lazily.

By "loops over input lazily" I mean that the incoming iterable shouldn't be looped over all at once (see the last line in the code block below).
```
>>> numbers_and_words = enumerate([99, 98, 97])
>>> flattened = deep_flatten(numbers_and_words)
>>> next(flattened)
0
>>> next(flattened)
99
>>> next(numbers_and_words)
(1, 98)
```
## Bonus 3
Note: We don't recommend this bonus for Advanced-level users, unless you need an extra challenge.

For the third bonus, I'd like you to make sure _deep flatten_ works with strings:
```
>>> list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']]))
['apple', 'pickle', 'pear', 'avocado']
```
## Hints
- [Differentiating types of iterables](https://stackoverflow.com/questions/1835018/how-to-check-if-an-object-is-a-list-or-tuple-but-not-string "isinstance can help determine whether an object is a certain type")
- [Flattening a list-of-lists](https://treyhunner.com/2021/11/how-to-flatten-a-list-in-python/ "On shallow flattening (not quite what we want)")
- [Bonus 1: Checking whether a given item is an iterable](https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable/1952481#1952481 "A few techniques for identifying whether a given object is an iterable")
- [Bonus 2: Making a function that returns an iterator](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/ "Generators are the easy way to make iterators")
- [Bonus 3: Why strings are weird](https://twitter.com/treyhunner/status/1455579995112452099 "Strings are infinitely recursive data structures")