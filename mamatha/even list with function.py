def check_number(n,m):
    i=0
    while i<len(n):
      if n[i]%2==0 and m[i]%2==0:
        print("even")
      else:
        print("not even")
      i=i+1
n=[2,6,18,10,3,75]
m=[6,19,24,12,3,87]
check_number(n,m)