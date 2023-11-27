def xor_range(L, R):
    result = L
    for i in range(L + 1, R + 1):
        result = result ^ i
    return result

# Example usage:
L = 1
R = 5
print(xor_range(L, R))  # Output will be 1
