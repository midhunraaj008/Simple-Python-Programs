n=int(input("Enter the order of the Matrix : "))
matrix = [[0 for x in range(0,n)] for y in range(0,n)]
print("Enter Matrix : ")
for i in range(0,n):
    for j in range(0,n):
        matrix[i][j]=int(input("Enter element : "))
    matrix[i].sort()
x=int(input("Enter the element to search : "))
for i in range(0,n):
    for j in range(0,n):
        if(x==matrix[i][j]):
            print("Element found at position ({},{})".format(i+1,j+1))
            a=1
            break
if(a!=1):
    print("Element not found")
            