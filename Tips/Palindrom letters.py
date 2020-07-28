OriginalWord = input("Enter a word : ")

word = OriginalWord.lower()
lastIndex = word.__len__()-1
firstIndex = 0
pal = 1
while firstIndex<lastIndex:
    if word[firstIndex]!=word[lastIndex]:
        pal = 0
        break
    firstIndex = firstIndex+1
    lastIndex = lastIndex-1

if pal:
    print(OriginalWord,"is a palindrom")
else:
    print(OriginalWord,"is not a palindrom")
