#!/usr/bin/python3

for a in range(0, 9):
    for b in range(a + 1, 10):
        # Exemple : si a = 1, b commence à 2 pour éviter les doublons
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}".format(a, b), end=", ")
