haystack = "sadbutsad"
needle = "sad"      # for test

try:
    print(haystack.index(needle))     #return instead
except Exception:
    print(-1)    #return instead