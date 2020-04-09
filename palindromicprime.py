n=int(input("Enter the number : "))
temp=n
rem=rev=flag=0
i=2
while(temp!=0):
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
while(i<=n/2):
    if(n%i==0):
        flag=1
        break
    i=i+1
if(n==rev and flag==0):
    print("{} is a palindromic prime".format(n))
else:
    print("{} is not a palindromic prime".format(n))


