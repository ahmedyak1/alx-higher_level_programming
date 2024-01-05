#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(lof_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        lof_integers (list): a list of integer
    Returns:
        int: peak(s)
    """
    l = lof_integers
    # if there is no list of integers return None
    if l == []:
        return None
    length = len(l)

    s, e = 0, length - 1
    while s < e:
        mid = s + (e - s) // 2
        if l[mid] > l[mid - 1] and l[mid] > l[mid + 1]:
            return l[mid]
        if l[mid - 1] > l[mid + 1]:
            e = mid
        else:
            s = mid + 1
    return l[s]
