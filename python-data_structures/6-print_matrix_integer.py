#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for i, thing in enumerate(a):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(thing), end="")
        print()
