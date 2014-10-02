def p45():
  starting = 143
  n = 1000 * 1000
  tri = [(n * (n + 1))/2 for n in xrange(starting, n)]
  pen = [(n * (3 * n - 1))/2 for n in xrange(starting, n)]
  hexa = [(n * (2 * n - 1)) for n in xrange(starting, n)]
  return set(tri).intersection(set(pen)).intersection(set(hexa))
