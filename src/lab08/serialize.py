from models import Student
from pathlib import Path
import json


def students_to_json(students, path):
    path = Path(path)
    data = [s.to_dict() for s in students]
    if not data:
        raise ValueError("Нет такого")
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    return 'Файл успешно создан'

def students_from_json(json_path):
    ans = []
    if json_path[-4:] != "json":
        raise ValueError(f"Неверный тип файла {json_path}")
    

    json_path = Path(json_path)
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        for std in data:
            std = Student.from_dict(std)
            ans.append(std)
            
    except json.decoder.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    return ans


BFF = Student("Николай", "2007-03-19", "BIVT-25-5", 3.22)
I = Student('Мишаня', '2008-01-22', 'BIVT-25-5', 3.42)
GFomBF = Student('Кристина', '2008-06-19', 'BIVT-25-5', 5.00)

stds = [I, BFF, GFomBF]
# print(students_to_json(stds, '/Users/vasya/Downloads/MISiS-Proga1-main/data/lab08/students_input2.json'))
print(students_from_json('/Users/vasya/Downloads/MISiS-Proga1-main/data/lab08/students_input2.json'))