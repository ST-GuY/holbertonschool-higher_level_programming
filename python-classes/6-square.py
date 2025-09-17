#!/usr/bin/python3
"""4-square module that defines a Square class."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec taille et position optionnelles."""
        self.size = size  # Utilise le setter → vérification automatique
        self.position = position

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)


