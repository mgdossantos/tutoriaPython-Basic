# Develop a program that asks the user for three different words
# and prints them in alphabetical order.

word1 = input("Word 1: ")
word2 = input("Word 2: ")
word3 = input("Word 3: ")

# Store the words in a list
word_list = [word1, word2, word3]

print("Words before sorting:", word_list)

# Sort the list alphabetically
sorted_words = sorted(word_list)

print("Words in alphabetical order:", sorted_words)