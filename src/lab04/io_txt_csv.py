from pathlib import Path
import csv
import sys
sys.path.append(r'/Users/vasya/Downloads/MISiS-Proga1-main/src/lab03/src')
from A import *

def read_txt(path, encoding='utf-8'):
    p = Path(path)
    try:
        return normalize(p.read_text(encoding=encoding),True,True)
    except FileNotFoundError:
        print(f'файл {p} не найден')
        return ''
    except UnicodeDecodeError:
        print (f'неверная кодировка')
        return ''

all_text = read_txt('/Users/vasya/Downloads/MISiS-Proga1-main/src/lab04/text', 'utf-8')

def write_csv(rows, path, header = None):
    p= Path(path)
    # if path[-4:] == '.csv':
        # print (f'неверный формат')
        # return ''
    rows = list(rows)
    with p.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        else:
            header = ('word','count')
            w.writerow(header)
        for r in rows:
            if len(r) == 2:
                w.writerow(r)
            else:
                return ValueError
        return ''
    
data = []
for i in top_n(count_freq(tokenize(all_text)), 5):
    data.append(((f'{i[0]}'),(f'{i[1]}')))

print(data)    
print(write_csv(data,'/Users/vasya/Downloads/MISiS-Proga1-main/src/lab04/io_txt_csv_report', ('word', 'count')))