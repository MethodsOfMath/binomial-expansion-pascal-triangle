def pascaltriangle(n):
  # Produces Pascal's Triangle to row n starting at row 0  
    if n == 0:
        return [[1]]
    row = [1]
    triangle = [[1],[1,1]]
    if n == 1:
        return triangle
    for r in range(2,n+1):
        row = [1]
        for i in range (0,r-1):
            row.append(triangle[r-1][i] + triangle[r-1][i+1])
        row.append(1)
        triangle.append(row)
    return triangle
pascaltriangle(5)
def binomialExpand(x,y,r):
  #expands (x + y)^r using Pascal's Triangle 
    row = pascaltriangle(r)[r]
    sum = 0
    for i in range(r+1):
        sum += x^i*y^(r-i)*row[i]
    return sum
# change this part
var('x y')
binomialExpand(x,y,4)
