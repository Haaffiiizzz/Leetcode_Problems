words = ["alice","bob","charlie"]
s = "abc"         # for test

abbrev = ""
for word in words:
    abbrev += word[0]
    
print(abbrev == s)      # return instead   