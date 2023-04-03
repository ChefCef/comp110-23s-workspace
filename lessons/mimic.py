""""Input a string, it returns same string back to you"""

def mimic(my_words: str) -> str:
    """"Returns same string back to you"""
    return my_words

mimic("Hello!")

print(mimic("Hello!"))

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)
