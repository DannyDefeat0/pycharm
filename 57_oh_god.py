from fractions import Fraction

longer_numerators = 0

fraction = Fraction(1, 2)
for _ in range(1000):
    #each step includes a changing ratio
    fraction = Fraction(1, 2 + fraction)
    #and a constant one, only the ratio should change
    tmp = fraction + 1
    if len(str(tmp.numerator)) > len(str(tmp.denominator)):
        print(_+1, tmp)
        longer_numerators += 1

print(longer_numerators)