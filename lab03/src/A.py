def normalize(text, casefold, yo2e):
    text = text.replace("\t"," ")
    text = text.replace("\r"," ")
    text = text.replace("\n"," ")
    # text = text.replace("  "," ")
    text = ' '.join(text.split())
    
    if yo2e:
        text = text.replace("ё","е")
        text = text.replace("Ё","Е")
    if casefold:
        text = text.casefold()
    
    return text

# print(normalize('ПрИвЕт\nМИр\t',True,True))
# print(normalize('ёжик, Ёлка',True,True))
# print(normalize('Hello\r\nWorld',True,True))
# print(normalize('двойные   пробелы',True,True))



def tokenize(text):
    text = text.replace(',',' ')
    text = text.replace('.',' ')
    text = text.replace('!',' ')
    text = text.replace('?',' ')
    text = text.replace('—',' ')
    splittxt = text.split()
    a=[]
    for i in splittxt:
        if i[0].isdigit()==0 and i[0].isalpha() == 0 and i[0].isalnum()==0:
            continue
        else:
            a.append(i)
    return a

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

def count_freq(alp):
    words=[]
    wordcount=[]
    answer={}

    for i in alp:
        if i in words: continue
        else: words.append(i)
    
    for i in words:
        wordcount.append(alp.count(i))
    
    for i in range(len(words)):
        answer.update({words[i] : wordcount[i]})
    return answer

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(dict):
    sortedByAlpha = sorted(dict.items(), key=lambda x: x[0])
    sortedByCount = sorted(sortedByAlpha, key=lambda x: x[1], reverse=True)
    return sortedByCount

# print(top_n(count_freq(["a","b","a","c","b","a"])))
# print(top_n(count_freq(["bb","aa","bb","aa","cc"])))