import string
def pig_it(text):
    new_text=[]
    text = text.split()
    for i in text:
        if i not in string.punctuation:
            i = i[1:len(i)] + i[0] + "ay"
        new_text.append(i)
    return " ".join(new_text)

pig_it('O tempora o mores !')