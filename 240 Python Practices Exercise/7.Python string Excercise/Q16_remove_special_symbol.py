"""Exercise 16: Remove special symbols / punctuation from a string
"""

import string

def remove_punctuation(input_string):
    return ''.join(char for char in input_string if char not in string.punctuation)

# Example usage
input_string = "Hello, world! How's everything going?"
result = remove_punctuation(input_string)
print(result)  # Output: Hello world Hows everything going
