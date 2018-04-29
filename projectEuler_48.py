# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


def sumSerie(num):
  nums=[]  
  for i in range(1,num+1):
    nums.append(i**i)
  s=str(sum(nums))
  return s[-10:len(s)]
  
  
print(sumSerie(1000))
