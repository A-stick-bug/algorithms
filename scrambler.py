from random import randint

def scramble(word):
    word_letters = list(word)

    for i in range(len(word)):
        key = randint(0, len(word) - 1)
        key2 = randint(0, len(word) - 1)

        temp_value = word_letters[key]
        word_letters[key] = word_letters[key2]
        word_letters[key2] = temp_value

        new_word = "".join(word_letters)
        print(new_word)


print(scramble("Hello World!!!"))