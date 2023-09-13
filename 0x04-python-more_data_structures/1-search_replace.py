#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listnew = list(map(lambda k: replace if k == search else k, my_list))
    return (listnew)

