#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_li = set(my_list)
    number = 0

    for k in unique_li:
        number += k
    return (number)

