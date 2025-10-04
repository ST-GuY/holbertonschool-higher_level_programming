#!/usr/bin/python3
"""
Module 12-pascal_triangle
Contient une fonction qui génère le triangle de Pascal.
"""


def pascal_triangle(n):
    """
    Retourne une liste de listes d'entiers représentant le triangle de Pascal.

    Args:
        n (int): Le nombre de lignes du triangle.

    Returns:
        list: Une liste de listes d'entiers représentant le triangle.
              Si n <= 0, retourne une liste vide.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
