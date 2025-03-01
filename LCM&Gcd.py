import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
a, b = 12, 18
print(lcm(a, b), gcd(a, b))  # Output: 36 6
