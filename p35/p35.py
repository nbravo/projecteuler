def getPrimes(num):
  primes = [True] * num
  primes[0] = False
  primes[1] = False

  for i in xrange(len(primes)):
    if primes[i]:
      multFactor = 2
      nextPrime = i
      while (multFactor * nextPrime < len(primes)):
        primes[multFactor * nextPrime] = False
        multFactor += 1
  return primes

def getRotations(num):
  numAsList = list(str(num))
  rotations = []
  i = 0
  while (i < len(numAsList)):
    numAsList.insert(0, numAsList.pop())
    rotations.append(list(numAsList))
    i += 1
  return list(set([int(''.join(rotation)) for rotation in rotations]))

def p35():
  primes = getPrimes(1000 * 1000)
  numRotationalPrimes = 0
  for i in xrange(2, len(primes)):
    if primes[i]:
      rotations = getRotations(i)
      if all([primes[i] for i in rotations]):
        numRotationalPrimes += 1
  return numRotationalPrimes
