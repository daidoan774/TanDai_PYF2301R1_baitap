def count_word_occurrences(text, word):
    count = text.count(word)
    return count

text = "Python is a popular programming language. Python"
word = "Python"

result = count_word_occurrences(text, word)

print(f"The word '{word}' appears {result} times in the text.")
