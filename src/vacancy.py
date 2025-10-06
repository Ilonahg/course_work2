class Vacancy:
    """
    Класс, описывающий вакансию.

    Attributes:
        title (str): Название вакансии.
        url (str): Ссылка на вакансию.
        salary (int): Уровень заработной платы.
        description (str): Краткое описание вакансии.
    """

    __slots__ = ["title", "url", "salary", "description"]

    def __init__(self, title: str, url: str, salary: dict | None, description: str):
        """
        Инициализация объекта Vacancy.

        Args:
            title (str): Название вакансии.
            url (str): Ссылка на вакансию.
            salary (dict | None): Информация о зарплате.
            description (str): Краткое описание вакансии.
        """
        self.title = title
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.description = description or "Описание отсутствует"

    def __validate_salary(self, salary_data):
        """
        Проверяет и возвращает корректное значение зарплаты.

        Args:
            salary_data (dict | None): Словарь с данными о зарплате.

        Returns:
            int: Минимальное значение зарплаты или 0, если данных нет.
        """
        if not salary_data:
            return 0
        return salary_data.get("from") or 0

    def __lt__(self, other):
        """
        Сравнение вакансий по зарплате (меньше).

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True, если зарплата меньше.
        """
        return self.salary < other.salary

    def __gt__(self, other):
        """
        Сравнение вакансий по зарплате (больше).

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True, если зарплата больше.
        """
        return self.salary > other.salary

    def __eq__(self, other):
        """
        Проверка равенства вакансий по зарплате.

        Args:
            other (Vacancy): Другая вакансия для сравнения.

        Returns:
            bool: True, если зарплаты равны.
        """
        return self.salary == other.salary

    def __repr__(self):
        """
        Возвращает строковое представление объекта Vacancy.

        Returns:
            str: Текст с названием, зарплатой и ссылкой.
        """
        return f"{self.title} | Зарплата: {self.salary} | {self.url}"

    @classmethod
    def cast_to_object_list(cls, vacancies_json: list):
        """
        Преобразует список JSON-данных вакансий в объекты класса Vacancy.

        Args:
            vacancies_json (list): Список вакансий в формате JSON.

        Returns:
            list[Vacancy]: Список объектов Vacancy.
        """
        vacancies = []
        for v in vacancies_json:
            vacancies.append(
                cls(
                    v["name"],
                    v["alternate_url"],
                    v.get("salary"),
                    v.get("snippet", {}).get("requirement", "")
                )
            )
        return vacancies
