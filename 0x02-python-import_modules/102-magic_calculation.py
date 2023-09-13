#!/usr/bin/python3


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a >= b:
		tot = sub(a, b)
        return(tot)
    else:
		number = add(a, b)
        for k in range(4, 6):
            number = add(number, k)
        return (number)

