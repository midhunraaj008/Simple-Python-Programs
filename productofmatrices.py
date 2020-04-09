n=int(input("Enter the order of the Matrix : "))
product=0
matrixA = [[0 for x in range(0,n)] for y in range(0,n)]
matrixB = [[0 for x in range(0,n)] for y in range(0,n)]
matrixR = [[0 for x in range(0,n)] for y in range(0,n)]
print("Enter Matrix A :")
for i in range(0,n):
    for j in range(0,n):
        matrixA[i][j]=int(input("Enter A[{}][{}] : ".format(i+1,j+1)))
print("\nEnter Matrix B :")
for i in range(0,n):
    for j in range(0,n):
        matrixB[i][j]=int(input("Enter B[{}][{}] : ".format(i+1,j+1)))
print("\nProduct of matrix A and B :")
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            product=product+(matrixA[i][k]*matrixB[k][j])
        matrixR[i][j]=product
        product=0
        print(matrixR[i][j],end=' ')
    print()        

