word = "aaAbcBC"    # for test

special = []
for letter in word:
    if letter in special:
        pass
    elif letter.islower() and letter.upper() in word:
        special.append(letter)

print(len(special))      # return instead