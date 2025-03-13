def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
sentence = "Find the longest word in this sentence."
print(longest_word(sentence))  # Output: "sentence"
