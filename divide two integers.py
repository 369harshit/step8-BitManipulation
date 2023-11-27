def divide(dividend, divisor):
    # Sign of the quotient
    if (dividend < 0) ^ (divisor < 0):
        sign = -1 
    else:
        sign = 1

    # Convert both numbers to positive
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return sign * quotient

# Example usage
dividend = 10
divisor = 3
result = divide(dividend, divisor)
print("Output:", result)
