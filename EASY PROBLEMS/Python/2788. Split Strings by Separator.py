words = ["one.two.three","four.five","six"]
separator = "."     # for test

final = []
for string in words:
    splitWord = string.split(separator)
    for word in splitWord:
        if word:
            final.append(word)
    
print(final)         # return instead