import json
import pytest
from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_saver import JSONSaver
from src.utils import sort_vacancies, filter_vacancies, get_top_vacancies


@pytest.fixture
def sample_vacancies():
    """Создаёт тестовые вакансии"""
    return [
        Vacancy("Python Developer", "url1", {"from": 150000}, "Опыт с Django"),
        Vacancy("Backend Developer", "url2", {"from": 80000}, "Flask и FastAPI"),
        Vacancy("Junior Developer", "url3", {"from": 50000}, "без опыта"),
    ]


def test_vacancy_validation():
    v = Vacancy("Test", "url", None, "")
    assert v.salary == 0
    assert isinstance(v.salary, int)


def test_vacancy_comparison(sample_vacancies):
    v1, v2, v3 = sample_vacancies
    assert v1 > v2
    assert v3 < v1


def test_sort_vacancies(sample_vacancies):
    sorted_list = sort_vacancies(sample_vacancies)
    assert sorted_list[0].salary == 150000
    assert sorted_list[-1].salary == 50000


def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["Django"])
    assert len(filtered) == 1
    assert "Django" in filtered[0].description


def test_get_top_vacancies(sample_vacancies):
    top = get_top_vacancies(sample_vacancies, 2)
    assert len(top) == 2


def test_json_saver(tmp_path, sample_vacancies):
    test_file = tmp_path / "test_vacancies.json"
    saver = JSONSaver(filename=str(test_file))

    for v in sample_vacancies:
        saver.add_vacancy(v)

    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 3

    saver.delete_vacancy(sample_vacancies[0])

    with open(test_file, "r", encoding="utf-8") as f:
        new_data = json.load(f)

    assert len(new_data) == 2


def test_hh_api_request():
    api = HeadHunterAPI()
    result = api.get_vacancies("Python")
    assert isinstance(result, list)
    assert "name" in result[0]
