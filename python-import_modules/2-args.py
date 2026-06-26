#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nb = len(argv) - 1
    if nb == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(nb, "s" if nb > 1 else ""))
        for i in range(1, nb + 1):
            print("{}: {}".format(i, argv[i]))
