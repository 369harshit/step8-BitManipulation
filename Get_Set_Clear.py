def get_bit(num, i):
    bit_at_k = 1 << (i - 1)
    bit = (num & bit_at_k) >> (i - 1)
    return bit

def set_bit(num, i):
    bit_at_k = 1 << (i - 1)
    num |= bit_at_k
    return num

def clear_bit(num, i):
    bit_at_k = ~(1 << (i - 1))
    num = num & bit_at_k
    return num

num = 25
i = 3

print(get_bit(num, i),end=" ")       # Output: 0
num = set_bit(num, i)
print(num, end=" ")                  # Output: 29
num = clear_bit(num, i)
print(num)                           # Output: 25
