def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

N = int(input("Enter N: "))
M = int(input("Enter M: "))

print("Result:", multiply_n_iterations(N, M))
