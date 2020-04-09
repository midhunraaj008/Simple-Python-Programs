limit=int(input("Enter the limit : "))
count=1
i=2
while(count<=limit):
    flag=0
    j=2
    while(j>=2 and j<=(i/2)):
        if(i%j==0):
            flag=1
            break
        j=j+1
    if(flag==0):
        print(i)
        count=count+1
    i=i+1
