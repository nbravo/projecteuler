def p81(fileName):
  matrix = fileToMatrix(fileName)
  memo = memoize(matrix)
  return memo[(0, 0)]

def memoize(matrix):
  memo = {}
  size = len(matrix)
  for i in xrange(size - 1, -1, -1):
    for j in xrange(size - 1, -1, -1):
      if (i == size - 1) and (j == size - 1):
        memo[(i, j)] = matrix[i][j]
      elif (i == size - 1) and (j < size - 1):
        memo[(i, j)] = matrix[i][j] + memo[(i, j + 1)]
      elif (j == size - 1) and (i < size - 1):
        memo[(i, j)] = matrix[i][j] + memo[(i + 1, j)]
      else: # anywhere in the matrix besides the last column or last row
        memo[(i, j)] = matrix[i][j] + min(memo[(i + 1, j)], memo[(i, j + 1)])
  return memo


def fileToMatrix(fileName):
  with open(fileName) as f:
    content = f.readlines()

  matrix = []
  for item in content:
    matrix.append(map(int, item.strip('\n').split(',')))
  return matrix
