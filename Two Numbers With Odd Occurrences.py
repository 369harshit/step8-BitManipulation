def find_odd_occurrences(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    odd_occurrences = []
    for key, value in freq.items():
        if value % 2 != 0:
            odd_occurrences.append(key)

    odd_occurrences.sort(reverse=True)
    return odd_occurrences

# Example usage:
arr = [3, 3, 1, 2]
result = find_odd_occurrences(arr)
print(result)  # Output will be [2, 1]
