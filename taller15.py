# Python program to find the inverse of matrix.
 
# Function to Print matrix.
def PrintMatrix(ar, n, m):
    for i in range(n):
        for j in range(m):
            print(ar[i][j], end="  ")
        print()
    return
 
# Function to Print inverse matrix
def PrintInverse(ar, n, m):
    for i in range(n):
        for j in range(n, m):
            print("%.3f  " % ar[i][j], end="")
        print()
    return
 
# Function to perform the inverse operation on the matrix.
def InverseOfMatrix(matrix, order):
    # PrintMatrix function to print the element of the matrix.
    print("=== Matrix ===")
    PrintMatrix(matrix, order, order)
 
    # Create the augmented matrix
    for i in range(order):
        for j in range(2 * order):
            # Add '1' at the diagonal places of the matrix to create an identity matrix
            if j == (i + order):
                matrix[i][j] = 1
 
    # Interchange the row of matrix, interchanging of row will start from the last row
    for i in range(order - 1, 0, -1):
        if matrix[i - 1][0] < matrix[i][0]:
            tempArr = matrix[i]
            matrix[i] = matrix[i - 1]
            matrix[i - 1] = tempArr
 
    # Print matrix after interchange operations.
    print("\n=== Augmented Matrix ===")
    PrintMatrix(matrix, order, order * 2)
 
    # Replace a row by the sum of itself and a
    for i in range(order):
        for j in range(order):
            if j != i:
                temp = matrix[j][i] / matrix[i][i]
                for k in range(2 * order):
                    matrix[j][k] -= matrix[i][k] * temp
 
    for i in range(order):
        temp = matrix[i][i]
        for j in range(2 * order):
            matrix[i][j] = matrix[i][j] / temp
 
    # print the resultant Inverse matrix.
    print("\n=== Inverse Matrix ===")
    PrintInverse(matrix, order, 2 * order)
 
    return
 
# Driver code
def main():
    order = 3
 
    matrix = [[0 for i in range(20)] for j in range(20)]
 
    matrix[0][0] = 3
    matrix[0][1] = 2
    matrix[0][2] = 2
    matrix[1][0] = 3
    matrix[1][1] = 1
    matrix[1][2] = -3
    matrix[2][0] = 1
    matrix[2][1] = 0
    matrix[2][2] = -2
 
    # Get the inverse of matrix
    InverseOfMatrix(matrix, order)
 
if __name__ == '__main__':
    main()