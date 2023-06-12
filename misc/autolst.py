#This script automatically creates the /dupl/ paths for a .lst file
import os
    
#https://stackoverflow.com/questions/35091557/replace-nth-occurrence-of-substring-in-string
def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

with open("assets\\FMOD_GOF2_LOUNGE_eng.lst", 'r') as f:

    contents = f.read()
    contentList = contents.split("\n")

    #key = filename
    #value = number of instances
    words = {}

    for i in contentList:

        if i not in words:
            words[i] = 1

        else:
            words[i] = words[i] + 1
            contents = nth_repl(contents, i, "dupl"+str(words[i])+"\\"+i, words[i] )

    f.close()

with open("assets\\FMOD_GOF2_LOUNGE_eng.lst", 'w') as f: 
    print(contents)
    f.write(contents)

    f.close()