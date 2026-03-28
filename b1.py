n=0
num=100
for i in range(1,n+1,1):
    r=num%10
    num=num//10
print(r,end="")