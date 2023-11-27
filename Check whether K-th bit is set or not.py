def is_kth_bit_set(n, k):
    # Shifting 1 to left by k-1 positions to check the k-th bit
    bit_at_k = 1 << (k - 1)
    # Performing bitwise AND operation to check if the k-th bit is set
    if (n & bit_at_k) > 0:
        return True
    else:
        return False

# Example usage:
N = 5
K = 3
result = is_kth_bit_set(N, K)
if result:
    print(f"The {K}-th bit is set in {N}")
else:
    print(f"The {K}-th bit is not set in {N}")
