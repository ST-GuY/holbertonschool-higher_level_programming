#!/usr/bin/python3

for a in range(97, 123):
    # N'imprime pas les lettres 'q' et 'e'
    if chr(a) not in ['q', 'e']:
        print("{}".format(chr(a)), end='')
