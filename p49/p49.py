import itertools

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
  finalPrimes = []
  for index in xrange(len(primes)):
    if primes[index]:
      finalPrimes.append(index)
  return finalPrimes

def p49():
  allPrimes = getPrimes(10 * 1000)
  relevantPrimes = [i for i in allPrimes if len(str(i)) == 4]
  diffs = {}
  for pair in list(itertools.combinations(relevantPrimes, 2)):
    diff = abs(pair[0] - pair[1])
    if diff in diffs:
      currList = diffs[diff]
      currList.extend([pair[0], pair[1]])
      diffs[diff] = currList
    else:
      diffs[diff] = [pair[0], pair[1]]
  newDiffs = {}
  for key in diffs:
    if key <= 4500:
      values = diffs[key]
      values = list(set(values))
      newValues = [i for i in values if (i + 2*key < 10 * 1000)]
      if newValues != []:
        newDiffs[key] = newValues
  for key in newDiffs:
    for cand in newDiffs[key]:
      cand2 = cand + key
      cand3 = cand + 2 * key
      if cand in relevantPrimes and cand2 in relevantPrimes and cand3 in relevantPrimes:
        if set(list(str(cand))) == set(list(str(cand2))) and set(list(str(cand2))) == set(list(str(cand3))):
          return (cand, cand2, cand3)
