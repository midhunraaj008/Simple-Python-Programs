import math
x=int(input("Enter the number : "))
n=int(input("Enter the limit : "))
def series(a,b):
    f=r=1
    result=0
    for i in range (1,n+1):
        f=f*i
        r=x**i
        result=result+(r/f)
    return result
print("The sum of the series is ",series(x,n))
