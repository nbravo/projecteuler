def p67(fileName):
  tri = getTriangle(fileName)
  memo = memoize(tri)
  return memo[(0, 0)]

def getTriangle(fileName):
  with open(fileName) as f:
    content = f.readlines()

  tri = []
  for row in content:
    tri.append(map(int, row.strip('\n').split(' ')))
  return tri

def memoize(triangle):
  memo = {}
  triSize = len(triangle)
  for i in xrange(triSize - 1, -1, -1):
    for j in xrange(len(triangle[i])):
      if i == triSize - 1: # bottom row
        memo[(i,j)] = triangle[i][j]
      else: # somewhere up in the triangle
        memo[(i,j)] = triangle[i][j] + max(memo[(i + 1, j)], memo[(i + 1, j + 1)])
  return memo
