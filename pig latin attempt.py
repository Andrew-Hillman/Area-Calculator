sentence = input('enter a sentence: ')
for word in sentence.split():
    print(word)

    if word [0] in 'aeiou' :
        print(f"{word} starts with a vowel")
    else:
        print(f"{word} does not start with a vowel")
