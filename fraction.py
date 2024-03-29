import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if type(numerator) is not int:
            raise TypeError("numerator must be an integer")
        if type(denominator) is not int:
            raise TypeError("denominator must be an integer")

        self.numerator = numerator
        self.denominator = denominator

        self.simplify()

    def simplify(self):
        """Simplify self value by dividing both numerator and denominator
        with its greatest common factor.
        """
        gcd = math.gcd(self.numerator, self.denominator)

        if self.denominator == 0:
            self.denominator = math.nan
        else:
            self.numerator = int(self.numerator/gcd)
            self.denominator = int(self.denominator/gcd)

    def is_nan(self):
        """Return boolean idicating whether the value is nan or not
        """
        return math.isnan(self.numerator/self.denominator)

    def __str__(self):
        """Return a string in a form of self.numerator/self.denominator
        or return in an integer form if the denominator is 1, -1 or the
        numerator is 0
        or return nan if the denominator is 0
        """
        is_able_to_write_in_integer_form = (
            abs(self.denominator) == 1) or self.numerator == 0
        is_negative = (self.numerator < 0) != (self.denominator < 0)

        if self.is_nan():
            return str(math.nan)

        if is_able_to_write_in_integer_form:
            integer_form = str(int(self.numerator/self.denominator))
            return integer_form

        if is_negative:
            return f"-{abs(self.numerator)}/{abs(self.denominator)}"

        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """Return a string in a form of 'Fraction(a, b)'
        """
        if self.is_nan():
            return f"Fraction({self.numerator}, 0)"

        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, fraction):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        first_fraction_in_decimal = self.numerator/self.denominator
        second_fraction_in_decimal = fraction.numerator/fraction.denominator

        return first_fraction_in_decimal == second_fraction_in_decimal

    def __add__(self, fraction):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if self.is_nan() or fraction.is_nan():
            return math.nan

        result_numerator = (self.numerator*fraction.denominator) + \
            (self.denominator*fraction.numerator)
        result_denominator = (self.denominator*fraction.denominator)

        result_fraction = Fraction(result_numerator, result_denominator)

        return result_fraction

    def __sub__(self, fraction):
        """Return the subtracted fraction of two fractions as a new fraction.
           Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        if self.is_nan() or fraction.is_nan():
            return math.nan

        result_numerator = (self.numerator * fraction.denominator) - \
            (self.denominator * fraction.numerator)
        result_denominator = (self.denominator * fraction.denominator)

        result_fraction = Fraction(result_numerator, result_denominator)

        return result_fraction

    def __mul__(self, fraction):
        """Return the multiplication of two fractions as a new fraction.
        Use the standard formula a/b * c/d = (a*c)/(b*d)
        """
        if self.is_nan() or fraction.is_nan():
            return math.nan

        product_numerator = self.numerator * fraction.numerator
        product_denominator = self.denominator * fraction.denominator

        product = Fraction(product_numerator, product_denominator)

        return product

    def __truediv__(self, fraction):
        """Return the division of two fractions as a new fraction.
        Use the standard formula a/b / c/d = (a/b)*(d/c)
        """
        if self.is_nan() or fraction.is_nan():
            return math.nan

        diviser_fraction = Fraction(fraction.denominator, fraction.numerator)

        return self * diviser_fraction

    def __gt__(self, fraction):
        """Return a boolean idicating whether self-value is
        greater than the input fraction or not by covert
        both fractions into decimal forms and compare them
        with > operator
        """
        self_decimal_form = self.numerator/self.denominator
        comparing_fraction_decimal_form = fraction.numerator/fraction.denominator

        return self_decimal_form > comparing_fraction_decimal_form

    def __lt__(self, fraction):
        """Return a boolean idicating whether self-value is
        less than the input fraction or not by covert
        both fractions into decimal forms and compare them
        with < operator
        """
        self_decimal_form = self.numerator/self.denominator
        comparing_fraction_decimal_form = fraction.numerator/fraction.denominator

        return self_decimal_form < comparing_fraction_decimal_form

    def __neg__(self):
        """Return the a new fraction by multiplied the initial
        fraction with -1
        """
        return self * Fraction(-1, 1)
