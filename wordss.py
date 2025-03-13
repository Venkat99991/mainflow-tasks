def count_words(sentence):
    words = sentence.split()
    return len(words)

# Example
sentence = "Count how many words are in this sentence."
print(count_words(sentence))  # Output: 8
