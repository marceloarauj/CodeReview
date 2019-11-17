l=[]
b=int(input("Enter a number: "))
while(b>0):
    dig=b%10
    l.append(dig)
    b=b//10
print("Sum is:")
print(sum(l))