import json
import os
from abc import ABC, abstractmethod
from vacancy import Vacancy


class AbstractSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass


class JSONSaver(AbstractSaver):
    """Сохранение вакансий в JSON"""

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def add_vacancy(self, vacancy: Vacancy):
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # проверка на дубли
        if any(v["url"] == vacancy.url for v in data):
            return

        data.append({
            "title": vacancy.title,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "description": vacancy.description
        })

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_vacancies(self, keyword: str):
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [v for v in data if keyword.lower() in v["title"].lower()]

    def delete_vacancy(self, vacancy: Vacancy):
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        data = [v for v in data if v["url"] != vacancy.url]

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
