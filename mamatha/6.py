def calculator(number1,number2):
    c=[]
    i=0
    mul=0
    while i<len(number1):
        mul=(number1[i]*number2[i])
        c.append(mul)
        i=i+1
    print(c)
calculator(number1=[5,10,50,20],number2=[2,20,3,5])