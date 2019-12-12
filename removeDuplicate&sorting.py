def removeDuplicate(input):
     newSentence = []
     words = input.split(" ")
     for word in sorted(set(words)):
         newSentence.append(word)

     return " ".join(newSentence)
print(removeDuplicate('hello world and practice makes perfect and hello world again'))

