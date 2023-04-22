#!/usr/bin/python3
"""
Finds a peak (highest number) in an unsorted list
"""


def find_peak(list_of_integers):
    """
    Finds peak in a list of ints
    """
    size = len(list_of_integers)
    half = size // 2
    half_e = size

    if size == 0:
        return None

    while True:
        half_e = half_e // 2
        if (half < size - 1 and
                list_of_integers[half] < list_of_integers[half + 1]):
            if half_e // 2 == 0:
                half_e = 2
            half = half + half_e // 2
        elif half_e > 0 and list_of_integers[half] < list_of_integers[half - 1]:
            if half_e // 2 == 0:
                half_e = 2
            half = half - half_e // 2
        else:
            return list_of_integers[mid]

