# Problem Statement
This exercise includes **3 bonuses** and **7 hints** (hover over the hint links before clicking on them).

I'd like you to write a function called _parse ranges_, which accepts a string containing ranges of numbers and returns an iterable of those numbers.

The numeric ranges in the string will consist of two numbers separated by hyphens and each of the ranges will be separated by commas and any number of spaces.

Your function should work like this:
```
>>> parse_ranges('1-2,4-4,8-13')
[1, 2, 4, 8, 9, 10, 11, 12, 13]
>>> parse_ranges('0-0, 4-8, 20-20, 43-45')
[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
```
In the examples above the functions return lists of numbers. Your function can return any iterable of numbers that you'd like though.

If you finish the main problem, try to solve at least one of the bonuses.
## Bonus 1
For the first bonus, I'd like you to return an iterator (like a generator, not a list) from your function.

You could make a generator function to do this or you could return a generator expression.
```
>>> numbers = parse_ranges('100-10000')
>>> next(numbers)
100
>>> next(numbers)
101
```
## Bonus 2
For the second bonus, I'd like you to allow individual numbers as well as pairs of two numbers:
```
>>> list(parse_ranges('0,4-8,20,43-45'))
[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
```
## Bonus 3
For the third bonus I'd like you to do something a bit odd: handle [coverage.py](https://coverage.readthedocs.io/en/6.3.2/) output that's similar to these numeric ranges.

The coverage.py program (used for measuring Python code coverage when testing) produces ranges of numbers similar to the format we're working with. The output from coverage.py sometimes includes ASCII arrows to show that one line jumped to another part of the program.

For the third bonus I want you to modify your function so that it accepts ranges with a single number followed by an _->_ and a number or word and ignores the _->_ and the thing that comes after it.

For example we include 20 here, but ignore _->_ and _exit_:
```
>>> list(parse_ranges('0, 4-8, 20->exit, 43-45'))
[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]
```
## Hint
Hints for **when you get stuck** (hover over links to see what they're about):
- [Splitting delimited text](https://twitter.com/treyhunner/status/1225455750664916992 "str.split accepts an optional delimiter and returns back a list of strings")
- [Converting strings to integers](https://stackoverflow.com/questions/642154/how-to-convert-strings-into-integers/642169#642169 "The int built-in function converts strings to integers")
- [Returning an iterator from a function](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/ "Use a generator function")
- [Avoiding hard-coded indices](https://www.pythonmorsels.com/topics/tuple-unpacking/ "You can use tuple unpacking to give names to values instead of just using indexes")
- [Determining if an item is a pair or a single value](https://stackoverflow.com/questions/30423395/why-does-pythons-str-partition-return-the-separator/30423850#30423850 "str.partition can be used to split pairs and identify non-pairs at once")
- [Replacing the '->' things](https://www.pythonforbeginners.com/regex/regular-expressions-in-python "You'll likely need a regular expression to do this particular text substitution")
- [Another approach for omitting '->'](https://pycon2017.regex.training/re-module.html#multi-search "Instead of substituting, you could use re.findall to only find the parts you're looking for")