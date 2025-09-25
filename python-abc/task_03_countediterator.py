#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.__iterable = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self  # permet d'utiliser l'objet dans une boucle for

    def __next__(self):
        item = next(self.__iterable)  # lève StopIteration quand fini
        self.count += 1
        return item

    def get_count(self):
        return self.count
