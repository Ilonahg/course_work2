# 🧠 Курсовая работа: Интеграция с API hh.ru

Проект выполнен в рамках курса по Python.  
Цель — получить и обработать вакансии с сайта **hh.ru**, сохранить их в файл,  
а также реализовать фильтрацию и сортировку вакансий по зарплате и ключевым словам.

---

## 🚀 Функционал

- Получение данных с API hh.ru (`requests`)
- Сохранение вакансий в JSON без дублей
- Класс `Vacancy` с валидацией и сравнением по зарплате
- Фильтрация и сортировка вакансий
- Консольное взаимодействие с пользователем
- Полное покрытие тестами (`pytest`, `pytest-cov`)

---

## 🧩 Структура проекта

course_work/
│
├── api.py # Работа с API hh.ru
├── vacancy.py # Класс Vacancy
├── file_saver.py # Сохранение вакансий в JSON
├── utils.py # Вспомогательные функции
├── main.py # Точка входа (интерфейс)
├── test_main.py # Тесты pytest
├── requirements.txt
└── README.md

 

---

## ⚙️ Установка и запуск

1. Клонировать репозиторий или скачать архив:
   ```bash
   git clone https://github.com/Ilonahg/course_work2.git
Перейти в папку проекта и установить зависимости:

 
pip install -r requirements.txt
Запустить проект:

 
python main.py
Ввести запросы:

 
Введите поисковый запрос (например, Python)
Введите количество вакансий для вывода в топ N
Введите ключевые слова для фильтрации (через пробел)
📊 Тестирование
Для запуска всех тестов:

 
pytest -v
Для отчёта о покрытии:

 
pytest --cov=. --cov-report=term-missing
Для HTML-отчёта:

 
pytest --cov=. --cov-report=html
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

👨‍💻 Автор
ФИО:  Гогильчин Илона Дмитриевна
GitHub: https://github.com/Ilonahg/course_work2.git
🏁 Статус проекта
✅ Завершён и готов к сдаче

 

```bash
git init
git add .
git commit -m "Initial commit: hh.ru API integration project"
git branch -M main
git remote add origin https://github.com/<твой-логин>/<название-репозитория>.git
git push -u origin main