def unique_prime_factors(N):
    factors = set()
    divisor = 2

    while N > 1:
        if N % divisor == 0:
            factors.add(divisor)
            while N % divisor == 0:
                N = N // divisor
        divisor += 1

    sorted_factors = sorted(factors)
    print(f"Unique prime factors of {N} are: {sorted_factors}")
    return sorted_factors

# Example
result = unique_prime_factors(10)
print(result)
