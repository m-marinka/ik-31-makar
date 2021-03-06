## Lab_5: Автоматизація за допомогою Makefile VS Docker Compose

Makefile
--
1. Створюю папку `my_app` в якій буде знаходитися  проект. Створюю папку `tests` де будуть тести на перевірку працездатності. Копіюю файли з репозиторію `devops_course` у відповідні папки свого. Переглядаю файл `requirements.txt` у папці проекту та тестах. Цей файл містить залежності додатку, які необхідно встановити.
                                                                                                                                                                                                   
2. Перевіряю чи проект є працездатним, перейшовши у папку та після ініціалізації середовища виконую наступні команди:
    ```bash
    pipenv --python 3.7
    pipenv install -r requirements.txt
    pipenv run python app.py
    ```
   
    - Для виправлення помилки `redis.exceptions.ConnectionError`, що виникла при спробі запустити додатку, встановлюю `redis-server`, виконавши команду `sudo apt install redis-server`. Роблю зміни у конфігураційному файлі `/etc/redis/redis.conf`. Пропипую у файлі `/etc/hosts` перенаправлення запитів redis на локальну адресу `127.0.0.1 redis`;
    - Переконуюся, що головна сторінка працює:
        
    - Ініціалузовую середовище для тестів у іншій вкладці терміналу та запускаю їх командою:
        ```bash
        pipenv run pytest test_app.py --url http://localhost:5000
        ```
    - Для того, щоб тести працювали створюю папку `logs` і лог-файл `app.log` у папці з додатком. Після цього тести проходять успішно:
    - Видаляю всі файли, що створились в процесі запуску (Pipfile, Pipfile.lock);
    - Перевіряю роботу сайту, перейшовши на кожну із сторінок:
3. Створюю два Dockerfile з іменами як у репозиторі `devops_course` та Makefile, який допоможе автоматизувати процес розгортання.
4. Ознайомлююся із вмістом Dockerfile та Makefile та його директивами:
   
   - `STATES` і `REPO` - змінні які містять назви тегів та назву Docker Hub репозиторію відповідно; 
   - `.PHONY` - утиліта `make`, яка вказує файлу, що переліченні нище цілі не являються файлами;
   - `$(STATES)` - ціль, призначення для білду контейнера;
   - `run` - ціль, призначення для створення мережі, у якій буде працювати додаток; запуску додатку і сховища redis;
   - `test-app` - ціль для запуску тестів;
   - `docker-prune` - ціль для очистки ресурсів, що бути використанні при роботі `Docker`.
5. Створюю Docker імеджі для додатку та для тестів виконавши команду:
    ```bash
            make .PHONY
    ```
6. Запускаю додаток та, відкривши новий термінал, запускаю тести:
    ```bash
            make run
            make test-app
    ```
   - Переконуюся, що тести пройшли успішно:
   - Перевіряю роботу кожної сторінки вебсайту:
7. Зупиняю проект, натиснувши Ctrl+C, та очищаю всі ресурси Docker за допомогою команди:
    ```bash
            make docker-prune
    ```
8. Створюю директиву в `Makefile` для завантаження створених імеджів у Docker Hub репозиторій. Завантажую імеджі до репозиторію `mmarinka/lab5_devops` командою:
    ```bash
            make push
    ```
   - [Посилання на Docker Hub репозиторій](https://hub.docker.com/repository/docker/mmarinka/lab5_devops)
 
9.  Видаляю створені та завантаженні імеджі. Створюю директиву `delete-images` в `Makefile`, яка автоматизує процес видалення імеджів. 

Docker Compose
--
1. Створюю файл `docker-compose.yaml` у коренeвій папці проекту та заповнюю вмістом згідно прикладу. Проект за цим варіантом трохи відрізняється від першого тим, що у нього з'являється дві мережі: `secret` і `public`:
   
   - У мережі secret знаходяться app і redis. Отстанній не має доступу до зовнішніх ресурсів;
   - До мережі public відносяться `app` і `tests`. Таким чином `tests` i `redis` не мають доступу один до одного.

