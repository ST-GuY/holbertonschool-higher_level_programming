#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            print("{:3d}".format(elem), end=' ')
        print()
