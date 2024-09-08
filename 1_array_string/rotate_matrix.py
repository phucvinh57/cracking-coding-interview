# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def rotate_matrix(matrix: list) -> list:
    """
    Rotate the matrix by 90 degrees
    """
    # (0, n-1) -> (n-1, n-1) -> (n-1, 0) -> (0, 0)
    # (0, j) -> (j, n-1) -> (n-1, n-j) -> (n-j, 0)
    # (i, j) -> (j, n-i-1) -> (n-i-1, n-j-1) -> (n-j-1, i)
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp

    return matrix

print(rotate_matrix([
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]))
print(rotate_matrix([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]))