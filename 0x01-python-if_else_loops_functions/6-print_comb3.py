#!/usr/bin/python3
for k in range(9):
    for m in range(k + 1, 10):
        if k * 10 + m < 89:
            print("{:d}{:d}".format(k, m), end=", ")
print("{:d}".format(89))
