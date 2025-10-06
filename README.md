 🧠 Курсовая работа: Интеграция с API hh.ru

Проект выполнен в рамках курса по Python.
Цель: получить и обработать вакансии с сайта hh.ru, сохранить их в JSON-файл,
а также реализовать фильтрацию и сортировку вакансий по зарплате и ключевым словам.

🚀 Функционал

Получение данных с API hh.ru (requests)

Сохранение вакансий в JSON без дублей

Класс Vacancy с валидацией и сравнением по зарплате

Фильтрация и сортировка вакансий

Консольное взаимодействие с пользователем

Полное покрытие тестами (pytest, pytest-cov)

🧩 Структура проекта
course_work2/
│
├── src/
│   ├── api.py           # Работа с API hh.ru
│   ├── vacancy.py       # Класс Vacancy
│   ├── file_saver.py    # Сохранение вакансий в JSON
│   ├── utils.py         # Вспомогательные функции
│   └── main.py          # Точка входа (интерфейс)
│
├── tests/
│   └── test_main.py     # Тесты pytest
│
├── vacancies.json       # Сохранённые вакансии
├── requirements.txt
└── README.md

⚙️ Установка и запуск

Клонировать репозиторий или скачать архив:

git clone https://github.com/Ilonahg/course_work2.git
cd course_work2


Установить зависимости:

pip install -r requirements.txt


Запустить проект:

python -m src.main


Следовать инструкциям:

Введите поисковый запрос (например, Python)
Введите количество вакансий для вывода в топ N
Введите ключевые слова для фильтрации (через пробел)

📊 Тестирование

Запуск всех тестов:

pytest -v


Отчёт о покрытии:

pytest --cov=src --cov-report=term-missing


HTML-отчёт:

pytest --cov=src --cov-report=html

📁 Пример работы
Введите поисковый запрос (например, Python): Python
Введите количество вакансий для вывода в топ N: 5
Введите ключевые слова для фильтрации (через пробел): Django Flask


Топ вакансий:

Backend-разработчик | Зарплата: 120000 | https://hh.ru/vacancy/126133194
Python Developer / Backend (Junior) | Зарплата: 50000 | https://hh.ru/vacancy/126122414

🧱 Технологии

Python 3.11+

requests

pytest

pytest-cov

JSON

👩‍💻 Автор

ФИО: Гогильчин Илона Дмитриевна
GitHub: https://github.com/Ilonahg/course_work2

🏁 Статус проекта

✅ Завершён и готов к сдаче