#!/usr/bin/python3
'''
Error Case Function
'''


def errorCases(matrix, div):
    ''' create a list of lens of of arrays in matrix '''
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for array in matrix:
        for element in array:
            if type(element) != int and type(element) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


'''
matrix module
'''


def matrix_divided(matrix, div):
    ''' Returns new matrix with results of division of original matrix '''
    errorCases(matrix, div)
    newMatrix = []
    for array in matrix:
        newMatrix.append([round(quot / div, 2) for quot in array])
    return newMatrix
