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
