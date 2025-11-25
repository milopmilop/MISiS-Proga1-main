import argparse
import sys
from pathlib import Path
sys.path.append(r'/Users/vasya/Downloads/MISiS-Proga1-main/src/lab04/')
from io_txt_csv import*
sys.path.append(r'/Users/vasya/Downloads/MISiS-Proga1-main/src/lab03/src/A.py')
from A import*

def cat(file_path, count=False):
    number = 1
    try:
        with open(file_path, 'utf-8') as f:
            for i in f:
                if count != False:
                    print(f'{number}, {i.strip()}')
                else:
                    print(i.strip)
                number += 1
    except FileNotFoundError:
        return 'файл не найден'
    
def stats(file_path, top=5):
    file_path = Path(file_path)
    try:
        txt = read_txt(file_path)
        print(f'всего слов{len(tokenize(txt))}')
        print(f'Уникальных слов: {len(set(tokenize(txt)))}')
        print('Top-5:')
        for i in top_n(count_freq(tokenize(txt)), top):
            print(f'{i[0]}:{i[1]}')
    except FileNotFoundError:
        return f'Ошибка. файл {file_path} не найден!'


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """ Реализация команды cat """
    elif args.command == "stats":
        """ Реализация команды stats """
if __name__ == "__main__":
    main()