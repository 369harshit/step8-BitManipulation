def count_bit_flips(num1, num2):
    # XOR the two numbers to find the differing bits
    xor_result = num1 ^ num2
    
    # Count the number of set bits in the XOR result
    count = 0
    while xor_result:
        # Increment count if the least significant bit is set
        count += xor_result & 1
        # Right shift to check the next bit
        xor_result = xor_result >> 1
    
    return count

# Example usage
number1 = 10
number2 = 7
result = count_bit_flips(number1, number2)
print(f"Minimum bit flips needed: {result}")
