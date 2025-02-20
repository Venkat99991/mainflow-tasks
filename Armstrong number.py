
# Sum of two numbers
def sum_of_two_numbers(a, b):
    return a + b

# Determine if a number is odd or even
def odd_or_even(n):
    return "Even" if n % 2 == 0 else "Odd"

# Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Generate Fibonacci sequence
def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    while n > 0:
        fib_sequence.append(a)
        a, b = b, a + b
        n -= 1
    return fib_sequence

# Reverse a string
def reverse_string(s):
    return s[::-1]

# Test the functions
if __name__ == "__main__":
    # Test sum_of_two_numbers
    print("Sum of 3 and 5:", sum_of_two_numbers(3, 5))

    # Test odd_or_even
    print("7 is:", odd_or_even(7))
    print("10 is:", odd_or_even(10))

    # Test factorial
    print("Factorial of 5:", factorial(5))

    # Test fibonacci_sequence
    print("First 10 Fibonacci numbers:", fibonacci_sequence(10))

    # Test reverse_string
    print("Reverse of 'hello':", reverse_string('hello'))

