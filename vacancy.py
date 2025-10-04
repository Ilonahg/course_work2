class Vacancy:
    """Класс описывающий вакансию"""

    __slots__ = ["title", "url", "salary", "description"]

    def __init__(self, title: str, url: str, salary: dict | None, description: str):
        self.title = title
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.description = description or "Описание отсутствует"

    def __validate_salary(self, salary_data):
        if not salary_data:
            return 0
        return salary_data.get("from") or 0

    # методы сравнения по зарплате
    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __repr__(self):
        return f"{self.title} | Зарплата: {self.salary} | {self.url}"

    @classmethod
    def cast_to_object_list(cls, vacancies_json: list):
        """Преобразует JSON вакансий в список объектов Vacancy"""
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
