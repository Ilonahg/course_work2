from src.vacancy import Vacancy



def sort_vacancies(vacancies: list[Vacancy]):
    """
    Сортирует список вакансий по убыванию зарплаты.

    Args:
        vacancies (list[Vacancy]): Список объектов вакансий.

    Returns:
        list[Vacancy]: Отсортированный список вакансий.
    """
    return sorted(vacancies, reverse=True)


def filter_vacancies(vacancies: list[Vacancy], keywords: list[str]):
    """
    Фильтрует вакансии, оставляя только те, где в описании встречаются ключевые слова.

    Args:
        vacancies (list[Vacancy]): Список объектов вакансий.
        keywords (list[str]): Список ключевых слов для фильтрации.

    Returns:
        list[Vacancy]: Список отфильтрованных вакансий.
    """
    return [v for v in vacancies if any(k.lower() in v.description.lower() for k in keywords)]


def get_top_vacancies(vacancies: list[Vacancy], n: int):
    """
    Возвращает топ N вакансий из списка.

    Args:
        vacancies (list[Vacancy]): Список вакансий.
        n (int): Количество топ-вакансий для выбора.

    Returns:
        list[Vacancy]: Топ N вакансий.
    """
    return vacancies[:n]


def print_vacancies(vacancies: list[Vacancy]):
    """
    Выводит список вакансий в консоль.

    Args:
        vacancies (list[Vacancy]): Список вакансий для вывода.
    """
    for v in vacancies:
        print(v)
