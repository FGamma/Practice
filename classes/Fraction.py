class Fraction(object):
    """
    A class to represent a fraction.
    """

    def __init__(self, num, denom):
        """
        Initialize a Fraction instance.

        Args:
            num (int): The numerator of the fraction.
            denom (int): The denominator of the fraction. Must not be zero.
        """
        assert isinstance(num, int) and isinstance(denom, int), \
            "numerator and denominator should be integers."
        assert denom != 0, "denominator cannot be zero."
        self.num = num
        self.denom = denom

    @property
    def numerator(self) -> int:
        """Get the numerator."""
        return self.num

    @numerator.setter
    def numerator(self, new_num):
        """Set the numerator."""
        assert isinstance(new_num, int), "Numerator must be an integer."
        self.num = new_num

    @property
    def denominator(self) -> int:
        """Get the denominator."""
        return self.denom

    @denominator.setter
    def denominator(self, new_denom):
        """Set the denominator."""
        assert isinstance(new_denom, int) and new_denom != 0, \
            "Denominator must be a non-zero integer."
        self.denom = new_denom

    def __str__(self) -> str:
        """ Returns a string representation of self """
        return f"{self.num}/{self.denom}"

    def __float__(self) -> float:
        """ Returns a float value of the fraction """
        return self.num / self.denom

    def __add__(self, other) -> "Fraction":
        """
        Add two fractions and return a new Fraction instance.

        Args:
            other (Fraction): The fraction to add.

        Returns:
            Fraction: The result of the addition.
        """
        numerator = self.num * other.denom + self.denom * other.num
        denominator = self.denom * other.denom
        return Fraction(numerator, denominator)


a = Fraction(1, 3)
a.denominator = 4
print(a)
b = Fraction(3, 4)
print(b)
print(a + b)