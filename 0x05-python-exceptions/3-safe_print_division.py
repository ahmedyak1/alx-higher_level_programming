#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divis = a / b
    except (TypeError, ZeroDivisionError,FloatingPointError):
        divis = None
    finally:
        print("Inside result: {}".format(divis))
    return (divis)

