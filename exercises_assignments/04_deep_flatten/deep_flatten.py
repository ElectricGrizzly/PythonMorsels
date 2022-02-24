'''
Flattens any provided list, tuple, generator, set, or iterable data structure.

Written for Python Morsels Exercise/Assignment #4 "deep_flatten"

Functions:

    deep_flatten(iterable: Iterable) -> Generator
    - Returns a flattened iterable as a generator object.
'''

from typing import Iterable, Generator

def deep_flatten(iterable: Iterable) -> Generator:
    '''
    Converts any multileveled list, tuple, generator, set, or iterable structure as a generator object.

    Parameters:
        iterable (Iterable): Any list, tuple, generator, set, or iterable structure

    Returns:
        generator (Generator): flattened generator object of given iterable.
    '''
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            yield from deep_flatten(item)
        else:
            yield item