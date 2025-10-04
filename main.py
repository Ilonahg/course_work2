from api import HeadHunterAPI
from vacancy import Vacancy
from file_saver import JSONSaver
from utils import sort_vacancies, filter_vacancies, get_top_vacancies, print_vacancies


def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    search_query = input("Введите поисковый запрос (например, Python): ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации (через пробел): ").split()

    print("Получаем вакансии с hh.ru...")
    vacancies_json = hh_api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(vacancies_json)

    # сохраняем в файл
    for v in vacancies:
        json_saver.add_vacancy(v)

    filtered = filter_vacancies(vacancies, filter_words)
    sorted_vacancies = sort_vacancies(filtered)
    top = get_top_vacancies(sorted_vacancies, top_n)

    print("\nТоп вакансий:")
    print_vacancies(top)


if __name__ == "__main__":
    user_interaction()
