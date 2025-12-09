from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self):
        """Валидация формата даты и диапазона GPA"""
        # Проверка формата даты (YYYY-MM-DD)
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        
        # Проверка диапазона GPA
        if not 0 <= self.gpa <= 5:
            raise ValueError("GPA должен быть в диапазоне 0-5")
    
    def age(self) -> int:
        """Вернуть количество полных лет"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d")
        today = datetime.now()
        
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> Dict:
        """Сериализация в словарь"""
        return {
            'fio': self.fio,
            'birthdate': self.birthdate,
            'group': self.group,
            'gpa': self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Десериализация из словаря"""
        return cls(**data)
    
    def __str__(self) -> str:
        """Красивый вывод"""
        return (f"Студент: {self.fio}\n"
                f"Дата рождения: {self.birthdate}\n"
                f"Группа: {self.group}\n"
                f"Средний балл: {self.gpa}")