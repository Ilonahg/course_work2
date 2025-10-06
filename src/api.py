import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный базовый класс для работы с API сайтов вакансий."""

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Абстрактный метод для получения списка вакансий по ключевому слову.

        Args:
            keyword (str): Ключевое слово для поиска вакансий.

        Returns:
            list: Список вакансий, полученных с API.
        """
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для взаимодействия с API сайта hh.ru."""

    __base_url = "https://api.hh.ru/vacancies"

    def __get_response(self, keyword: str):
        """
        Отправляет GET-запрос к API hh.ru и получает ответ в формате JSON.

        Args:
            keyword (str): Ключевое слово для поиска вакансий.

        Raises:
            Exception: Если код ответа HTTP не равен 200.

        Returns:
            dict: Ответ API в формате JSON.
        """
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
        """
        Возвращает список вакансий по указанному ключевому слову.

        Args:
            keyword (str): Ключевое слово для поиска вакансий.

        Returns:
            list: Список вакансий из API hh.ru.
        """
        data = self.__get_response(keyword)
        return data["items"]
