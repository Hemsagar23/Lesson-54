def multiply_M_iterations(N, M):
    result = 0
    for _ in range(M):
        result += N
    return result


def multiply_N_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result


# Example
N = 5
M = 7

print("Using M iterations:", multiply_M_iterations(N, M))
print("Using N iterations:", multiply_N_iterations(N, M))
