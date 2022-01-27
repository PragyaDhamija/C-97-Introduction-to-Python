name = input("Hi, What is your name?")
characterCount = 0
wordCount = 1
for i in name:
    characterCount+=1
    if(i==' '):
        wordCount+=1
print(characterCount)
print(wordCount)
