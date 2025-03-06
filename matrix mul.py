A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
print("Matrix Multiplication:", result)
