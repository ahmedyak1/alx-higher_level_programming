#!/usr/bin/python3

if _name_ == "_main_":
    import hidden_4

    noms = dir(hidden_4)
    for name in noms:
        if name[:2] != "__":
            print(name)
