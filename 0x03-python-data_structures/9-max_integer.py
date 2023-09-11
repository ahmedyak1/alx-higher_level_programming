#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        big_int_list = my_list[0]
        for item in range(len(my_list)):
            if my_list[item] > big_int_list:
                big_int_list = my_list[item]

    return (big_int_list)
