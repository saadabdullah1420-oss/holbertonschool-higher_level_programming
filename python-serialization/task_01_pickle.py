#!/usr/bin/env python3
"""Serialize and deserialize custom objects using pickle."""

import pickle


class CustomObject:
    """Represent a custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize this object and save it to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError, TypeError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an object from a file or return None on failure."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if not isinstance(obj, cls):
                return None
            return obj
        except (
            OSError,
            pickle.PickleError,
            EOFError,
            AttributeError,
            ImportError,
            IndexError,
            ValueError,
            TypeError,
        ):
            return None
