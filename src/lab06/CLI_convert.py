import argparse
import sys
from pathlib import Path
sys.path.append(r'C:\Users\vasya\Downloads\MISiS-Proga1-main\src\lab04\io_txt_csv.py')
from io_txt_csv import*
sys.path.append(r'C:\Users\vasya\Downloads\MISiS-Proga1-main\src\lab03\src\A.py')
from A import*
sys.path.append(r'C:\Users\vasya\Downloads\MISiS-Proga1-main\src\lab05')
from json_csv import*
from csv_xlsx import*

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.out)

    elif args.command == "scv2json":
        csv_to_json(args.input, args.out)

    elif args.commnd == 'csv2xlsx':
        csv_to_xlsx(args.input, args.out)

if __name__ == '__main__':
    main()