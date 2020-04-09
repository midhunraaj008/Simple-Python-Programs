n=int(input("Enter the order of the Matrix : "))
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
print("\nSum of Matrix A and B :")
for i in range(0,n):
    for j in range(0,n):
        matrixR[i][j]=matrixA[i][j]+matrixB[i][j]
        print(matrixR[i][j],end=' ')
    print()        

        
        