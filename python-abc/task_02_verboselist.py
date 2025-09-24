#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, x):
        print(f"Extended the list with [{len(x)}] items.")
        super().extend(x)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]      # récupérer l'élément avant suppression
        super().pop(index)      # supprimer l'élément
        print(f"Popped [{item}] from the list.")
        return item             # retourner l'élément supprimé
