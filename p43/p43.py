import itertools

def p43():
  satisfies = []
  for d in map(list, list(itertools.permutations(range(10)))):
    if conc([d[1], d[2], d[3]]) % 2 == 0 and \
      conc([d[2], d[3], d[4]]) % 3 == 0 and \
      conc([d[3], d[4], d[5]]) % 5 == 0 and \
      conc([d[4], d[5], d[6]]) % 7 == 0 and \
      conc([d[5], d[6], d[7]]) % 11 == 0 and \
      conc([d[6], d[7], d[8]]) % 13 == 0 and \
      conc([d[7], d[8], d[9]]) % 17 == 0:
      satisfies.append(conc(d))
  return sum(satisfies)
      

def conc(numList):
  return int(''.join(map(str, numList)))
