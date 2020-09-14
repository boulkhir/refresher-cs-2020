from math import gcd

class Fraction:

    n = 0
    d = 1

    def __init__(self, n, d):
        if d == 0:
            raise NameError('Division by 0')
        elif d > 0 :
            self.n = int(n / gcd(n, d))
            self.d = int(d / gcd(n, d))
        else:
            self.n = int(-n / gcd(n, d))
            self.d = int(-d / gcd(n, d))
            
    
    def multiply(self, frac):
        return Fraction(self.n * frac.n, self.d * frac.d)

    def add(self, frac):
        if self.d == frac.d:
            return Fraction(self.n + frac.n, self.d)
        else:
            dCommon = self.d * frac.d
            sn = self.n*frac.d
            fn = frac.n*self.d
            return Fraction(sn + fn, dCommon)
    
    def __add__(self, frac):
        return self.add(frac)

    def __mul__(self, frac):
        return self.multiply(frac)

    def __eq__(self, frac):
        return (self.n == frac.n) and (self.d == frac.d)

    def __lt__(self, frac):
        if self.d == frac.d :
            return self.n < frac.n
        else:
            s = self.n*frac.d
            f = frac.n*self.d
            return s < f

    def __str__(self):
        return str(self.n)+"/"+str(self.d)