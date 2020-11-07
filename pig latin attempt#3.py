userinput = input("Enter a word that starts with a vowel: ")

vowels = 'aeiou'

if userinput[0] in vowels:
    print(f"{userinput}way")
        
else:
    print(f"{userinput}ay")
