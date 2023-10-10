#!/usr/bin/python3
"""load modules"""
from sys import argv


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    jl = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    jl = []

for k in argv[1:]:
    jl.append(k)

save_file(jl, 'add_item.json')

