#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    len_sentence,first_index =len(sentence), sentence[0]
    return (len_sentence,first_index)
