# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

s=2**1000
s1=str(s)

count=0
for i in range(len(s1)):
  count+=int(s1[i])  

print(count)
