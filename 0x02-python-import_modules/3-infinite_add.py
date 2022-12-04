#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    count = len(sys.argv) - 1
    for i in range(count):
        add = add + int(sys.argv[i + 1])
    print(add)
