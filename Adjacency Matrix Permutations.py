from itertools import permutations


def permute(matrix, perm):
    """Permute the rows and columns of the matrix according to the permutation list."""
    n = len(matrix)
    # Create a new matrix to hold the permuted version
    permuted_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            permuted_matrix[i][j] = matrix[perm[i]][perm[j]]

    return permuted_matrix


def create_permutation_matrix(perm):
    """Create a permutation matrix from the permutation list."""
    n = len(perm)
    perm_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        perm_matrix[i][perm[i]] = 1
    return perm_matrix


def transpose(matrix):
    """Generate the transpose of a matrix."""
    n = len(matrix)
    return [[matrix[j][i] for j in range(n)] for i in range(n)]


def matrix_multiply(A, B):
    """Multiply two matrices A and B."""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return result


def are_isomorphic(adj_matrix1, adj_matrix2):
    n = len(adj_matrix1)

    # Ensure both matrices are of the same size
    if n != len(adj_matrix2):
        return False, None, None, None

    # Generate all possible permutations of vertex indices (0 to n-1)
    for perm in permutations(range(n)):
        # Apply the permutation on adj_matrix1
        permuted_matrix = permute(adj_matrix1, perm)

        # Compare the permuted matrix with adj_matrix2
        if permuted_matrix == adj_matrix2:
            perm_matrix = create_permutation_matrix(perm)
            perm_matrix_transpose = transpose(perm_matrix)

            # Calculate PAP^T
            result_matrix = matrix_multiply(matrix_multiply(perm_matrix, adj_matrix1), perm_matrix_transpose)
            return True, perm_matrix, perm_matrix_transpose, result_matrix

    return False, None, None, None


# Example 6x6 adjacency matrices for two graphs
adj_matrix1 = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 0]
]

adj_matrix2 = [
    [0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

# Check if the graphs are isomorphic and get the permutation matrix, its transpose, and the resulting matrix from PAP^T
result, perm_matrix, perm_matrix_transpose, result_matrix = are_isomorphic(adj_matrix1, adj_matrix2)

if result:
    print("The graphs are isomorphic.")
    print("Permutation matrix:")
    for row in perm_matrix:
        print(row)
    print("Transpose of the permutation matrix:")
    for row in perm_matrix_transpose:
        print(row)

    # Print the resulting matrix from PAP^T
    print("Resulting matrix from PAP^T:")
    for row in result_matrix:
        print(row)
else:
    print("The graphs are not isomorphic.")
