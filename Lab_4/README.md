# Lab_4: Робота з Docker

1. Для перевірки чи докер встановлений і працює правильно на віртуальній машині запускаю перевірку версії, виведення допомоги та тестовий імедж:
    ```bash
    docker -v
    docker -h
    docker run docker/whalesay cowsay Docker is fun
    ```
    - перенаправляю вивід цих команд у файл `my_work.log` та роблю коміт із ним до репозиторію.
    
2. Для знайомства з Docker створюю імедж із Django сайтом зробленим у попередній роботі.
    - Оскільки проект на Python то і базовий імедж також потрібно вибрати відповідний. Всі імеджі можна знайти на [Python Docker Hub](https://hub.docker.com/_/python). Використовую команду щоб завантажити базовий імедж з репозиторію: 
    ```bash
    docker pull python:3.7-slim
    docker images
    docker inspect python:3.7-slim
    ```
    - Створюю файл з іменем `Dockerfile` копіюю туди вміс такого ж файлу з репозиторію `devops_course`;
    - Ознайомлююся із коментарями та структурою написання Dockerfile;
    - Змінюю посилання на власний Git репозиторій із власним веб-сайтом та роблю коміт Dockerfile;
3. Створюю власний репозиторій на Docker Hub. Для цього логінюсь у власний аккаунт на Docker Hub, після чого переходжу у вкладку Repositories і далі натискаю кнопку `Create new repository`. Називаюи його `lab4-examples`.
4. Виконуюю білд (build) Docker імеджа та завантажую його до репозиторію. Для цього вказую правильну назву репозиторію та TAG. Команда буде виглядати (де `django` - це тег): 
    ```bash
    docker build -t mmarinka/lab4-examples:django .
    docker images
    dokcer push mmarinka/lab4-examples:django
    ```
   [Посилання на Docker репозиторій](https://hub.docker.com/repository/docker/mmarinka/lab4-examples)
   
   Посилання на скачування імеджа: `mmarinka/lab4-examples:django` ;
   
5. Для запуску веб-сайту потрібно виконую команду:
    ```bash
    docker run -it --name=django --rm -p 8000:8000 mmarinka/lab4-examples:django
    ``` 
    - перейдіть на адресу `http://127.0.0.1:8000` та переконуюсь що веб-сайт працює:
    
6. Оскільки веб-сайт готовий і працює, потрібно створити ще один контейнер із програмою моніторингу веб-сайту:

