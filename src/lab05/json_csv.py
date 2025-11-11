from pathlib import Path
import csv
import sys
import json
sys.path.append(r'/Users/vasya/Downloads/MISiS-Proga1-main/src/lab04/')
from io_txt_csv import *

def json_to_csv(json_path, csv_path):
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if not isinstance(data, list):
        raise 'FileError'
    
    header = [tuple(data[0].keys())]

    rows = []
    for i in data:
        rows.append(tuple(i.values()))

    write_csv(rows,csv_path,header ) #Lab04

# def scv_to_json(csv_)
print(json_to_csv('/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A.json','/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A.csv'))