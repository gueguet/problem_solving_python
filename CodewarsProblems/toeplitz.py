"""
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8 9
5 1 2 3 4 8
4 5 1 2 3 4
7 4 5 1 2 2
Write a program to determine whether a given input is a Toeplitz matrix.
"""

# we can first write a function which take a specific entry point of the matrix
# and check all the descending diagonal
def equal_diagonal(matrix, start_l, start_c):
    n = len(matrix)
    m = len(matrix[0])
    start = matrix[start_l][start_c]

    while start_l < n and start_c < m:
        if matrix[start_l][start_c] != start:
            return False
        else:
            start_l += 1
            start_c += 1
    
    return True


# and now apply it to the whole matrix
def isToeplitz(matrix):
    l, c = len(A), len(A[0])

    # go through the lines
    for row in range(l):
        # it should always been True otherwise we return Flase for the global method
        if not equal_diagonal(matrix, row, 0):
            return False

    # be careful we don't care about the first line this time
    for col in range(c):
        if not equal_diagonal(matrix, 0, col):
            return False

    return True
    

# test - A is Toeplitz
A = [[1, 3, 5],
     [-10, 1, 3],
     [2,-10,1]]

print(isToeplitz(A))

