#/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    for item in set(my_list):
        count += item
    return count
