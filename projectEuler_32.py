#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.



def isPan(num):
  n=[int(i) for i in str(num)]
  m=sorted(n)
  if n[0]!=0 and m==[x for x in range(1,10)]:
    return True
  else:
    return False

def prods():
  while True:
    comp=str(prod)+str(a)+str(b)
    if len(str(comp))<=9 and isPan(comp):
      
    
