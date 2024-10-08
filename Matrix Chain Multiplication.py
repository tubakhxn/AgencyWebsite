import sys

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for x in range(n)] for x in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n - 1]

# Example usage
p = [1, 2, 3, 4]
print(matrix_chain_order(p))  # Output: Minimum number of multiplications needed
