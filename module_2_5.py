def get_matrix(n, m, value):
    if n and m > 0:
        matrix = []
        for row in range(n):
            matrix.append([])
            for col in range(m):
                matrix[row].append(value)
        return matrix
    return []


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))