def set_rightmost_unset_bit(N):
    if N == 0:
        return 1

    bit_position = 0
    while N & (1 << bit_position) != 0:
        bit_position += 1

    return N | (1 << bit_position)

# Example
N = 5
result = set_rightmost_unset_bit(N)
print(result)  # Output: 7
