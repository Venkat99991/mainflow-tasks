n = int(input("Enter a decimal number: "))
binary = bin(n)[2:]  # Removes the "0b" prefix
print(f"Binary representation: {binary}")
