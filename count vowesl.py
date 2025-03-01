def count_vowels_and_consonants(s):
    vowels = 'aeiou'
    vowel_count = sum(1 for char in s.lower() if char in vowels)
    consonant_count = sum(1 for char in s.lower() if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Example usage
print(count_vowels_and_consonants("Hello, World!"))  # Output: (3, 7)
