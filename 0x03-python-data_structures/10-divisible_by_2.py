#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    numbers_divisible_by_2 = []
    for item in range(len(my_list)):
        if my_list[item] % 2 != 0:
            numbers_divisible_by_2.append(False)
        else:
           numbers_divisible_by_2.append(True) 
 return (numbers_divisible_by_2)
