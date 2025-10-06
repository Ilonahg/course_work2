import json
import os
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class AbstractSaver(ABC):
    """Абстрактный класс для работы с сохранением и загрузкой вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет вакансию в хранилище.

        Args:
            vacancy (Vacancy): Объект вакансии для добавления.
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Возвращает список вакансий, содержащих указанное ключевое слово.

        Args:
            keyword (str): Ключевое слово для фильтрации вакансий.

        Returns:
            list: Список найденных вакансий.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаляет вакансию из хранилища.

        Args:
            vacancy (Vacancy): Объект вакансии для удаления.
        """
        pass


class JSONSaver(AbstractSaver):
    """Класс для сохранения и управления вакансиями в JSON-файле."""

    def __init__(self, filename: str = "vacancies.json"):
        """
        Инициализирует объект JSONSaver.

        Args:
            filename (str): Имя JSON-файла для хранения вакансий.
        """
        self.__filename = filename
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет новую вакансию в JSON-файл, если она ещё не существует.

        Args:
            vacancy (Vacancy): Объект вакансии для добавления.
        """
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверка на дубли по URL
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
        """
        Ищет вакансии по ключевому слову в названии.

        Args:
            keyword (str): Ключевое слово для фильтрации вакансий.

        Returns:
            list: Список вакансий, содержащих ключевое слово.
        """
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [v for v in data if keyword.lower() in v["title"].lower()]

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаляет вакансию из JSON-файла по совпадению URL.

        Args:
            vacancy (Vacancy): Объект вакансии, который нужно удалить.
        """
        with open(self.__filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        data = [v for v in data if v["url"] != vacancy.url]

        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
