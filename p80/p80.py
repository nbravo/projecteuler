from decimal import *

def p80():
  squares = [i ** 2 for i in xrange(11)]
  currSum = 0
  for j in xrange(100):
    if j not in squares:
      currSum += digitalSum(j)
  return currSum

def digitalSum(n):
  getcontext().prec = 105
  decimalComponent = str(Decimal(n).sqrt()).replace('.', '')[:100]
  return sum(map(int, list(decimalComponent)))
