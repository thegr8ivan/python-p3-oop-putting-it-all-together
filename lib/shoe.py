#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, material):
        self.brand = brand
        self.size = size
        self.material = material
        self.condition = "Old"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or value <= 0:
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print(f"The {self.brand} shoe has been repaired.")
        self.condition = "New"
