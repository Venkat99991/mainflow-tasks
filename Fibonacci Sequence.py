def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
n = 6
print("Fibonacci sequence:", fibonacci_sequence(n))
