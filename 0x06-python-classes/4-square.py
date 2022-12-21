#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains a class called Square that defines a square."""


class Square:
    """This is the Square class definition."""

    def __init__(self, size=0):
        """__init__ method to initialize the size attribute.
        Args:
        size (int): Size of the square.
        """
        self.__size = size

        def area(self):
            """Calculate the area of the square.
            Returns:
            The area of the square.
            """
            return self.__size ** 2

        @property
        def size(self):
            """Getter method for the size attribute.
            Returns:
            The size of the square.
            """
            return self.__size

        @size.setter
        def size(self, value):
            """Setter method for the size attribute.
            Args:
            value (int): Size of the square.
            """
            if isinstance(value, int) is False:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
