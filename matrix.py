A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [10, 11, 12]]
result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Matrix Addition:", result)
