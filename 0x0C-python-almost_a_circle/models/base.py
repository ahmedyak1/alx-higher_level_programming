#!/usr/bin/python3
"""Class Base"""
import json
import turtle
import os.path as path
import csv 



class Base:
    """Class defines Base

     Attributes: define each inst
    """
    nbr_obj = 0

    def __init__(self, id=None):
        """new instance base

        Args: id : if of each inst
        """
        if id is not None:
            self.id = id
        else:
            Base.nbr_obj += 1
            self.id = Base.nbr_obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """return prest of list_dictionaries.

        Args: list of dictionaries.

        Returns: json string.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """sdout JSON string representation 

        Args:
            list_objs inst 
            list of Rectangle or list of Square inst
        """
        fn = "{}.json".format(cls.__name__)
        ld = []

        if not list_objs:
            pass
        else:
            for k in range(len(list_objs)):
            
                ld.append(list_objs[k].to_dictionary())


        l = cls.to_json_string(ld)

        with open(fn, 'w') as f:
            f.write(l)

    @staticmethod
    def from_json_string(json_string):
        """ Return list of the JSON string

        Args:
            json_string description

        Return:JSON string repre
        """
        if len(json_string) == 0 or json_string is None:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Return an insts with all parameters

        Args:
            dictionary  double pointer to a dictionary
            cls class

        Returns:
            list: an instance with all parameters 
        """
        if cls.__name__ == "Rectangle":
            d = cls(1, 1)
        if cls.__name__ == "Square":
            d = cls(1)
        d.update(**dictionary)
        return(d)

    @classmethod
    def load_from_file(cls):
        """Return a list of insta
        Args:
            cls class

        Return:list of inst
        """
        fn = "{}.json".format(cls.__name__)

        if path.exists(fn) is False:
            return []

        with open(fn, 'r') as ff:
            ls = ff.read()

        lc = cls.from_json_string(ls)
        li = []

        for k in range(len(lc)):
            li.append(cls.create(**lc[k]))

        return li

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serliaze a list of recta or squre 

        Args:cls class
             list_objs objects
        """
        fn = cls.__name__ + ".csv"
        with open(fn, 'w', newline="") as f:
            wri = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for k in list_objs:
                    wri.writerow([k.id, k.width, k.height, k.x, k.y])
            elif cls.__name__ == "Square":
                for k in list_objs:
                    wri.writerow([k.id, k.size, k.x, k.y])

    @classmethod
    def load_from_file_csv(cls):
        """deser a list of rectangles or square

        Args:cls class
        """
        fn = cls.__name__ + ".csv"
        mo = []
        try:
            with open(fn, 'r') as f:
                cr = csv.reader(f)
                for elm in cr:
                    if cls.__name__ == "Rectangle":
                        dictio = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictio = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obji = cls.create(**dictio)
                    mo.append(obji)
        except(Exception):
            pass
        return(mo)

