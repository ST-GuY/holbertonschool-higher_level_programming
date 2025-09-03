#!/usr/bin/python3

def uppercase(str):
    result = ""  # Initialisation d'une chaîne vide pour stocker le résultat final

    for c in str:  # Boucle sur chaque caractère 'c' de la chaîne d'entrée
        if 97 <= ord(c) <= 122:  # (ASCII de 'a' = 97 à 'z' = 122)
            result += chr(ord(c) - 32)  # Convertit la minuscule en majuscule
        else:
            result += c  # Si ce n'est pas une minuscule, on ajoute le caractère tel quel au résultat

    print("{}".format(result))  # Affiche la chaîne finale en majuscules
