# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


def testFifht(num):
  nums=[]
  for i in str(num):
    nums.append(int(i)**4)
    if sum(nums)!=num:
      return False
  return True

num=1500
fifths=[]
while num < 100000:
  if testFifht(num):
    fifths.append(num)
  num+=1

print(sum(fifths))
