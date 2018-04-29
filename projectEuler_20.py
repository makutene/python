# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def factorial(num):
  count=1
  for i in range(num,1,-1):
    count*=i
  return count

f=str(factorial(10))

def sum(string):
  sum=0
  for i in range(len(string)):
    sum+=int(string[i])
  print(sum)

sum(f)
