from vacancy import Vacancy


def sort_vacancies(vacancies: list[Vacancy]):
    return sorted(vacancies, reverse=True)


def filter_vacancies(vacancies: list[Vacancy], keywords: list[str]):
    return [v for v in vacancies if any(k.lower() in v.description.lower() for k in keywords)]


def get_top_vacancies(vacancies: list[Vacancy], n: int):
    return vacancies[:n]


def print_vacancies(vacancies: list[Vacancy]):
    for v in vacancies:
        print(v)
