Lab_2: Автоматизація. Знайомство з CI/CD.
-------
1. Створюю папку Lab_2 з README.md файлом.
2. Інсталюю pipenv за за допомогою пакетного менеджера PIP, використовуючи команду `pip install pipenv`.Створюю ізольоване середовище , використовуючи команду `pipenv --python 3.7`.Середовище запускаю , використовуючи команду `pipenv shell`.
3. Встановлюю біблотеки в ізольованому середовищі. Бібліотеку `requests` створюю, використовуючи команду `pipenv install requests`. Бібліотеку `ntplib` , використовуючи команду `pipenv install ntplib`.
4. В папці lab_2 створюю файл `app.py` і копіюю код програми з репозиторію. Запускаю програму командою `python app.py`. Програма працює правильно.
5. Встановлюю бібліотеку pytest за допомогою команди `pipenv install pytest`.
6. Копіюю тести, виконую їх використовуючи команду `pytest tests/tests.py`. Тести виконані успішно.
7. Для захисту дописую функцію, яка перевіряє Час доби. В залежності від часу доби PM/AM відображає Доброго дня/Доброї ночі.Дописую тест для перевірки виконання функції. 
8. Переношу результати виконання тестів та результат виконання програми у файл results.txt , використовуючи команди pytest tests/tests.py > results.txt та `python app.py >> results.txt.
9. Створюю Makefile, та заповнюю його для автоматизації процесу CI проекту.
10. Комічу Makefile. Колоную git репозиторій на віртуальну машину, та запускаю Makefile

