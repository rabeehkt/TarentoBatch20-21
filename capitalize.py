para = input()
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
new_para = ""
for word in para.split(' '):
    
    vowel = 0
    consonant=0
    for i in word:
        if i in vowels:
            vowel+=1
        if i in consonants:
            consonant+=1
    
    if(vowel>consonant):
        for i in word:
            if i in vowels:
                new_para+=i.upper()
            else:
                new_para+=i
    elif(consonant>vowel):
        for i in word:
            if i in consonants:
                new_para+=i.upper()
            else:
                new_para+=i
    else:
        new_para+=word.upper()
    new_para+=" "
print(new_para)