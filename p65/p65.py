from fractions import Fraction

def p65():
  convergents = []
  for k in xrange(1, 34):
    convergents.extend([1, 2 * k, 1])

  continuedFraction = Fraction()
  for num in convergents[::-1]:
    continuedFraction += num
    continuedFraction = reciprocal(continuedFraction)

  e = continuedFraction + 2
  return sum(map(int, list(str(e.numerator))))

def reciprocal(frac):
  return Fraction(frac.denominator, frac.numerator)
