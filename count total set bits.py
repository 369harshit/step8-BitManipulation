def count_set_bits(N):
    total_set_bits = 0
    for i in range(1, N + 1):
        # Counting set bits in the binary representation of each number
        num = i
        while num:
            total_set_bits += num & 1
            num = num >> 1
    return total_set_bits

N = 4
print(count_set_bits(N))  # Output: 5
