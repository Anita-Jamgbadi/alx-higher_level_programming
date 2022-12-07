#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    hold = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
           hold.append(key)
    for key in hold:
        del a_dictionary[key]
    return a_dictionary
