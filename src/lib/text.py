def normalize(text, casefold, yo2e):
    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    # text = text.replace("  "," ")
    text = " ".join(text.split())

    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")
    if casefold:
        text = text.casefold()

    return text


def tokenize(text):
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace("—", " ")
    splittxt = text.split()
    a = []
    for i in splittxt:
        if i[0].isdigit() == 0 and i[0].isalpha() == 0 and i[0].isalnum() == 0:
            continue
        else:
            a.append(i)
    return a


def count_freq(alp):
    words = []
    wordcount = []
    answer = {}

    for i in alp:
        if i in words:
            continue
        else:
            words.append(i)

    for i in words:
        wordcount.append(alp.count(i))

    for i in range(len(words)):
        answer.update({words[i]: wordcount[i]})
    return answer


def top_n(dict, n):
    ans = sorted(list(dict.items()), key=lambda x: (-x[1], x[0]))
    return ans[:n]
