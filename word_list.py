# Create a list of words
words = ["apple", "banana", "cherry", "mango", "orange", "grape", "avocado"]

# Use list comprehension to create a list of words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the list of words with odd number of characters
print(odd_length_words)
