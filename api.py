import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API hh.ru"""

    __base_url = "https://api.hh.ru/vacancies"

    def __get_response(self, keyword: str):
        params = {
            "text": keyword,
            "area": 113,  # Россия
            "per_page": 20
        }
        response = requests.get(self.__base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка запроса: {response.status_code}")
        return response.json()

    def get_vacancies(self, keyword: str):
        data = self.__get_response(keyword)
        return data["items"]
