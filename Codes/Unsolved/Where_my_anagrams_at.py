def anagrams(word, words):
    for i in words:
        tmp = word
        for letter in tmp:
            if letter not in tmp:
                words.remove(i)
                break
            else:
                tmp = tmp.replace(letter, '')
    return words


x = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(x)
