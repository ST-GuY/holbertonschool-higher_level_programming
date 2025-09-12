#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass  # On ignore les éléments qui ne sont pas des entiers
        finally:
            # On incrémente i dans tous les cas pour éviter une boucle infinie
            i += 1
    print()
    return count
