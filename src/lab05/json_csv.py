from pathlib import Path
import csv
import sys
import json

sys.path.append(r"/Users/vasya/Downloads/MISiS-Proga1-main/src/lab04/")
from io_txt_csv import *


def json_to_csv(json_path, csv_path):
    if json_path[-4:] != "json":
        return f"TypeError! неверный формат"
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    try:

        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list):
        raise "FileError"

    header = tuple(data[0].keys())

    rows = []
    for i in data:
        rows.append(tuple(i.values()))

    write_csv(rows, csv_path, header)  # Lab04
    return "файл создан"


# print(json_to_csv('/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A.json', '/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A.csv'))


def csv_to_json(csv_path, json_path):
    if csv_path[-4:] != f".csv":
        return "неверный файл"
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    try:
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            data = csv.DictReader(csv_file)
            rows = list(data)
    except:
        raise FileNotFoundError("Осутствующий файл")
    if not rows:
        return ValueError("Пустой CSV")
    if not data.fieldnames:
        return ValueError("CSV без заголовка")
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, indent=2)
    return "Файл создан"


# print(csv_to_json('/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A.csv','/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A1.json'))
