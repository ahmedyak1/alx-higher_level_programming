#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ordonee = list(a_dictionary.keys())
    list_ordonee.sort()
    for k in list_ordonee:
        print("{}: {}".format(k, a_dictionary.get(k)))

