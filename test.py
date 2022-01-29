
words = []

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    words.append(word)

if len(words) > 0:
    word_length_sum = 0

    for word in words:
        word_length_sum += len(word)

    average_word_length = word_length_sum / len(words)
    print(f"The average word length is: {average_word_length}.")
