#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    listnew = []
    for item in range(0, list_length):
        try:
            divi = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("out of range")
            divi = 0
            
        except TypeError:
            print("wrong type")
            divi = 0
            
        except ZeroDivisionError:
            print("division by 0")
            divi = 0
        
        finally:
            listnew.append(divi)
    return (listnew)

