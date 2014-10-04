import itertools

def p44():
  pen = [(n * (3 * n - 1))/2 for n in xrange(1, 7000)]
  candidates = []

  for pair in itertools.combinations(pen, 2):
    if (pair[0] + pair[1] in pen) and (abs(pair[0] - pair[1]) in pen):
      candidates.append(abs(pair[0] - pair[1]))

  return min(candidates)
