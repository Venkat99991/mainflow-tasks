def is_pythagorean_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

# Example
print(is_pythagorean_triplet(3, 4, 5))  # Output: True
