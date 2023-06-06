#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for value in range(len(matrix)):
        for x in range(len(matrix[value])):
            if not x:
                print("{:d}".format(matrix[value][j]), end="")
            else:
                print(" ".format(" "), end="")
                print("{:d}".format(matrix[value][j]), end="")
        print()