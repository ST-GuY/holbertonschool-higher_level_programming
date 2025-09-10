#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):  # Définition de la fonction avec une liste et un nombre par défaut
    # map applique une fonction (ici lambda) à chaque élément de my_list
    # lambda x: x * number -> prend chaque élément x et le multiplie par number
    # list(...) transforme l'objet map en une nouvelle liste (sans modifier my_list)
    return list(map(lambda x: x * number, my_list))
