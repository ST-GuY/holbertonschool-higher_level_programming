#!/usr/bin/python3

import sys               # On importe le module sys, qui permet d'accéder à sys.argv (la liste des arguments)


def main():

    nb_argument = len(sys.argv) - 1
    # On calcule le nombre d'arguments en enlevant le nom du script

    if nb_argument == 1:  # Si l'utilisateur a donné exactement 1 argument
        mot = "argument"  # alors on choisit le mot au singulier
    else:                 # sinon (0 ou plusieurs arguments)
        mot = "arguments"  # on choisit le mot au pluriel

    if nb_argument == 0:
        print(f"{nb_argument} {mot}.")
        # On affiche "0 arguments." avec un point
    else:
        print(f"{nb_argument} {mot}:")
        # On affiche par ex. "2 arguments:" avec un deux-points

# Parcourt les arguments donnés (en commençant à 1 car [0] = nom du script)
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
            # On affiche "numéro: valeur" pour chaque argument


# Assure que la fonction main() s'exécute seulement
# si on lance le fichier directement
if __name__ == "__main__":
    main()
