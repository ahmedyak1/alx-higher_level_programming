#!/usr/bin/python3
import hidden_4

if _name_ == "_main_":
    noms = dir(hidden_4)
    for nom in noms:
        if nom[:2] != "__":
            print(nom)
