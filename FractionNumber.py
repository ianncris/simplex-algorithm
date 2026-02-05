import math

class FractionNumber:
    def __init__(self, num, den = 1):
        self.num = num
        self.den = den

        if self.den < 0:
            self.num = -self.num
            self.den = -self.den
        
        if self.den != 0:
            gcd = math.gcd(abs(self.num), abs(self.den))
            self.num //= gcd
            self.den //= gcd
        else:
            self.num = 0
            self.den = 0
    
    def subtraction(self, otherFraction):
        num = self.num * otherFraction.den - otherFraction.num * self.den
        den = self.den * otherFraction.den
        new = FractionNumber(num, den)
        return new
    
    def multiplication(self, otherFraction):
        num = self.num * otherFraction.num
        den = self.den * otherFraction.den
        new = FractionNumber(num, den)
        return new
    
    def division(self, otherFraction):
        num = self.num * otherFraction.den
        den = self.den * otherFraction.num
        new = FractionNumber(num, den)
        return new

    def print_number(self):
        if self.den == 1:
            return f"{self.num}"
        elif self.den == 0:
            return "err"
        return f"{self.num}/{self.den}"
    
    def numerator(self):
        return self.num

    def denominator(self):
        return self.den
    
    def minor_major(self, otherFraction):
        return self.num * otherFraction.den < otherFraction.num * self.den