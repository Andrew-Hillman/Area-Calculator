userinput = input("Enter a word: ")

vowels = 'aeiou'
modifinput = userinput.strip()
if modifinput[0] in vowels:
    print(f"{modifinput}way")
        
else:
    i = 1
    while i < len(modifinput):
        print(modifinput[i], end = '')
        i = i + 1
    print(f"{modifinput[0]}ay")
