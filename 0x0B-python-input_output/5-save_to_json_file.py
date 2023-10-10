#!/usr/bin/python3
"""Function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """write obj using json prese

    Args:
        my_obj Object 
        filename name file 

    Returns: JSON 
    """

    with open(filename, 'w', encoding="utf-8") as f:
        
        jo = json.dumps(my_obj)
       
        f.write(jo)
        f.close()

