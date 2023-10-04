#!/usr/bin/python3
"""text indentation function
"""


def text_indentation(text):
    """sdout a text with twi new lines after char ?
    
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for dell in ".:?":
        text = (dell + "\n\n").join(
            [l.strip(" ") for l in text.split(dell)])

    print(text, end="")

