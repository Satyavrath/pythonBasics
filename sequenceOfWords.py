def seqOfWords(*input):
    list = []
    for word in sorted(input):
        list.append(word)

    return list

print(seqOfWords('without','hello','bag','world'))