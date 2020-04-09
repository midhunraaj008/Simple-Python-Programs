x=int(input("Enter the Base : "))
n=int(input("Enter the Limit : "))
def series(a,b):
    p=result=0
    f=1
    for i in range(1,(2*b),2):
        for j in range(1,i+1):
            f=f*j
        r=a**i
        result=result+(((-1)**p)*(r/f))
        p=p+1
        f=1
    return result
print("The sum of the series is ",series(x,n))
        
