#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    a = 0
    b = 0
    for tuplee in my_list:
        a += tuplee[0] * tuplee[1]
        b += tuplee[1]
    c = a / b
    return (c)

