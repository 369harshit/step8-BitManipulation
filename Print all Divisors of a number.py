def print_all_divisors(N):
    divisors = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    print(f"All divisors of {N} are: {divisors}")

# Example
print_all_divisors(5)
