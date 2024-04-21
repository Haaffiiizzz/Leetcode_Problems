title = "capiTalIze tHe titLe"       # for test

final = ""
for word in title.split()[:-1]:
    if len(word) < 3:
        word = word.lower()
        final += word + " "
        
    else:
        word = word[0].upper() + word[1:].lower()
        final += word + " "
        
if len(title.split()[-1]) < 3:
    word = title.split()[-1].lower()
    final += word
else:
    word = title.split()[-1][0].upper() + title.split()[-1][1:].lower()
    final += word

print(final)       # return instead       