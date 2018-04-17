pal=[]
for i in range(100,1000):
  for j in range(100,1000):
    res=str(i*j)
    if res[0:3]==res[:-1-3:-1] and len(res)==6:
      pal.append(res)
print(max(pal))
