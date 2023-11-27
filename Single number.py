def find_single_number(nums):
    result = 0
    for num in nums:
        result = result ^ num # Using bitwise XOR operation
    return result

# Example usage:
nums = [2,2,1]
print(find_single_number(nums))  # Output will be 4
