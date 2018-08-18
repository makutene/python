#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def printFac(num):
  a=1
  for i in range(num,1,-1):
    a*=i
  return a

def checksum(num):
  b=str(num)
  x=[]
  for i in b:
    x.append(printFac(i))
  if num == sum(x):
    return True
  return False
