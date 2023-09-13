#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    list_ke = list(a_dictionary.keys())

    for k in list_ke:
        number += 1

    return (number)
