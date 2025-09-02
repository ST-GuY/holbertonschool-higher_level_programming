#!/usr/bin/python3

for a in range(100):
    print("{:02}".format(a), end=', ' if a < 99 else '\n')
    # :02 rempli toujours avec deux chiffre
