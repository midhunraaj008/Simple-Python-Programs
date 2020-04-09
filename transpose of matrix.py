n=int(input("Enter the order of the Matrix : "))
matrixA = [[0 for x in range(0,n)] for y in range(0,n)]
matrixB = [[0 for x in range(0,n)] for y in range(0,n)]
print("Enter Matrix A :")
for i in range(0,n):
    for j in range(0,n):
        matrixA[i][j]=int(input("Enter A[{}][{}] : ".format(i+1,j+1)))
print("\nThe Transposed Matrix : ")
for i in range(0,n):
    for j in range(0,n):
        matrixB[i][j]=matrixA[j][i]
        print(matrixB[i][j],end=' ')
    print()        

