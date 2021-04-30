m=[1,1,2,2,3,3,4,5,4,5]
i=0
d=[]
while i<len(m):
    if m[i] not in d:
        d.append(m[i])
    i=i+1
print(d)
