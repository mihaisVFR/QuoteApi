# Развертывание на локальной машине
1. Установить pipenv `sudo apt update`, `apt install pipenv`
2. Создать виртуальное окружение и установить зависимости: `pipenv sync`
3. Запустить виртуальное окружение: `pipenv shell`
4. Создание локальной БД `pipenv run python  create_db.py`
5. Для заполнения таблицы Learners значениями `pipenv run python add_learners.py`