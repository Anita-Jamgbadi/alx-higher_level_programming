#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list) - 1
    if i == 0:
        return None
    else:
        while i > 0:
            j = 0
            while j < i:
                if my_list[j] > my_list[j + 1]:
                    tmp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = tmp
                j += 1
            i -= 1
    return my_list[len(my_list) - 1]
