import math

class FractionNumber:
    def __init__(self, num, den = 1):
        self.num = num
        self.den = den

        if self.den < 0:
            self.num = -self.num
            self.den = -self.den
        
        elif self.den != 0:
            gcd = math.gcd(abs(self.num), abs(self.den))
            self.num //= gcd
            self.den //= gcd
        
        elif self.den == 0:
            self.den = 1
            
        else:
            self.num = 0
            self.den = 0
    
    def subtract(self, otherFraction):
        num = self.num * otherFraction.den - otherFraction.num * self.den
        den = self.den * otherFraction.den
        new = FractionNumber(num, den)
        return new
    
    def multiply(self, otherFraction):
        num = self.num * otherFraction.num
        den = self.den * otherFraction.den
        new = FractionNumber(num, den)
        return new
    
    def divide(self, otherFraction):
        num = self.num * otherFraction.den
        den = self.den * otherFraction.num
        new = FractionNumber(num, den)
        return new

    def printnum(self):
        if self.den == 1:
            return f"{self.num}"
        elif self.den == 0:
            return "err"
        return f"{self.num}/{self.den}"
    
    def compare(self, otherFraction):
        return self.num * otherFraction.den < otherFraction.num * self.den