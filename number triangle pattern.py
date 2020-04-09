n=int(input("Enter no of Rows : "))
for i in range (1,n+1):
    k=i
    while(n-k)!=0:
        print(end='  ')
        k=k+1
    for j in range (1,(2*i)):
        if(j<=i):
            print(i+j-1,end=' ')
        if(j>i):
            print((j-i+1),end=' ')   
    print("\n")
