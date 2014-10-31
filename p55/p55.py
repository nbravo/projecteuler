def p55():
  numLychrelNumbers = 0
  for i in xrange(10 * 1000):
    if isLychrel(i):
      numLychrelNumbers += 1
  return numLychrelNumbers

def isLychrel(num):
  iterCount = 0
  while iterCount < 50:
    num += int(str(num)[::-1])
    if str(num) == str(num)[::-1]:
      return False
    iterCount += 1
  return True

print p55()
