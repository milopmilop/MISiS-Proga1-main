from A import normalize, tokenize, count_freq, top_n

fl = open('/Users/Мишаня/VSCProjects/MISiS-Proga1/lab03/src/text', encoding='utf-8').readline()

# print(f'всего слов:{len(normalize(fl,1,1))}')
print(f'всего слов: {len(tokenize(fl))}')
print(f'уникальных слов: {len(count_freq(tokenize(fl)))}')
print(f'топ пять:')
for i in top_n(count_freq(tokenize(fl))):
    print(f'{i[0]}:{i[1]}')

