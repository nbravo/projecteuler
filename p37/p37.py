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

def p37():
  numLimit = 1000 * 1000
  primes = getPrimes(numLimit)
  trunctablePrimes = []
  for i in xrange(10, numLimit):
    if trunctablePrime(i, primes):
      trunctablePrimes.append(i)
  return sum(trunctablePrimes)

def trunctablePrime(num, primes):
  numStr = str(num)
  numLen = len(numStr)
  left = 0
  while left < numLen:
    if not primes[int(numStr[left:])]:
      return False
    left += 1
  right = numLen
  while right > 0:
    if not primes[int(numStr[:right])]:
      return False
    right -= 1
  return True

print p37()
