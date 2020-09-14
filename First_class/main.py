from fraction import *

def main():
    #x1 = Fraction(0, 0)
    x2 = Fraction(2, 1)
    x3 = Fraction(-1, -2)
    x4 = Fraction(5, -15)
    x5 = Fraction(4, 2)
    x6 = Fraction(14, 13)
    x7 = Fraction(1, 1)
    x8 = Fraction(1, -2)

    # operations
    print( "x2 * x3 ="+str(x2 * x3 ))
    print( "x4 * x3 ="+str(x4 * x3 ))
    print( "x3 * x8 ="+str(x3 * x8 ))
    print( "x4 * x8 ="+str(x4 * x8 ))
    print( "x2 + x6 ="+str(x2 + x6 ))
    print( "x7 + x7 + x7 + x7 ="+str(x7 + x7 + x7 + x7 ))
    print( "x5 < x3 = "+str(x5<x3))
    print( "x4 < x8 = "+str(x4<x8))
    print( "x7 < x2 = "+str(x7<x2))
    print( "x5 == x2 = "+str(x5==x2))
    print( "x8 == x3 = "+str(x8==x3))



if __name__ == "__main__":
    # execute only if run as a script
    main()