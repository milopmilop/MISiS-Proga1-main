from pathlib import Path
import csv
import sys
import json
from openpyxl import Workbook

def csv_to_xlsx(csv_path, xlsx_path):
    if csv_path[-4:] != '.csv':
        return r'TypeError! неверный формат'
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)
    except FileNotFoundError:
        raise FileNotFoundError('Отсутствует файл')
    
    if not data:
        return 'ValueError! Пустой csv'
    
    header=data[0]

    if not header:
        return 'ValueError! пустой заголовок у csv'
    
    wb = Workbook()
    ws = wb.active
    for i in data:
        ws.append(i)
    wb.save(xlsx_path)
         
print(csv_to_xlsx('/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/A.csv','/Users/vasya/Downloads/MISiS-Proga1-main/src/lab05/B.xlsx'))