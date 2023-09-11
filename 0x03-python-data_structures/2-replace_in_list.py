#!/usr/bin/python3
"""
    Replace an item of a list at a specific index
    args:my_list,idx,element
"""
def replace_in_list(my_list, idx, element):
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return (my_list)

