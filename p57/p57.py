from fractions import Fraction

def p57():
  iterCounter = 0
  currExpansion = 1 + Fraction(1, 2)
  numSatisfying = 0
  while iterCounter < 1000:
    if len(str(currExpansion.numerator)) > len(str(currExpansion.denominator)):
      numSatisfying += 1
    currExpansion = 1 + reciprocal(1 + currExpansion)
    iterCounter += 1
  return numSatisfying

def reciprocal(frac):
  return Fraction(frac.denominator, frac.numerator)
