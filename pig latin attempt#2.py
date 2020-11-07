def sentence():
    
    sentence() = 'This is a sentence'
    vowels = 'aeiou'

    for word in sentence().split():
        firstLetter = word[0]

        if firstLetter in vowels:
            print(f"{​​firstLetter}​​ is a vowel")
        else:
            print(f"{​​firstLetter}​​ is not a vowel")
