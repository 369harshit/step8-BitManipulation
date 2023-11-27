def check_bit_set(n, k):
    # Shifting the bit at position k to the rightmost position (0th position)
    bit_at_k = (n >> k) & 1

    if bit_at_k == 1:
        return "SET"
    else:
        return "NOT SET"

# Input values
n = 5
k = 1

result = check_bit_set(n, k)
print(f"Output: {result}")
