#!/usr/bin/python3
"""A class MyInt"""


class MyInt(int):
    """Class inherits from int"""

    def __eq__(self, other):
        """checks for equality
        Args:
            other (int)
        Returns:
            True if equal, false otherwise
        """
        return self.real != other

    def __ne__(self, other):
        """Checks for inequality
        Args:
            other (int)
        Returns:
            True if unequal, false otherwise
        """
        return self.real == other
