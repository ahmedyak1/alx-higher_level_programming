#!/usr/bin/python3
"""
    Substitute an element in a duplicated list at a particular location
    args:my_list,idx,element
"""
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= (len(my_list)):
        return (my_list)
    copy_list_temp = my_list.copy()
    copy_list_temp[idx] = element
    return (copy_list_temp)
