#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for ligne in matrix:
        nouvelle_ligne = []
        for valeur in ligne:
            nouvelle_ligne.append(valeur * valeur)
        new_matrix.append(nouvelle_ligne)
    return new_matrix
