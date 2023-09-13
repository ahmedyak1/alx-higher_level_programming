#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dirrectory = a_dictionary.copy()
    list_ke = list(new_dirrectory.keys())

    for k in list_ke:
        new_dirrectory[k] *= 2
    return new_dirrectory

