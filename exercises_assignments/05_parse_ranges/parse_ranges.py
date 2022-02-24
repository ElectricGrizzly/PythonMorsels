'''
Parse a string of comma-separated integer ranges and returns a generated object of the given ranges.

Written for Python Morsels Exercise/Assignment #5 "parse_ranges"

Functions:

    parse_ranges(ranges_string: str) -> Generator
    - Returns a generated object of the given ranges
'''

from typing import Generator

def parse_ranges(ranges_string: str) -> Generator:
    '''
    Returns a generated object of the given ranges

    Parameters:
        ranges_string (str): A string of comma-separated integer ranges

    Returns:
        generator (Generator): A generator object of given integer ranges
    '''
    for value in [value.strip() for value in ranges_string.split(',')]:
        if '-' in value:
            first, last = value.split('-')
            if '>' in last:
                yield int(first)
            else:
                yield from range(int(first), int(last) + 1)
        else:
            yield int(value)