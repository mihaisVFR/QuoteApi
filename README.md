## Развертывание на локальной машине
1. Установить pipenv `sudo apt update`, `apt install pipenv`
2. Создать виртуальное окружение и установить зависимости: `pipenv sync`
3. Запустить виртуальное окружение: `pipenv shell`
4. Создание локальной БД `flask db init`,`flask db migrate -m "new db""`,`flask db upgrade`
5. Для заполнения таблицы Learners значениями `pipenv run python add_learners.py`

### Файлы с ДЗ расположены в ./day2_homework, модель в ./api/models
- [x] Напиcана схема которая сериализует экземпляр модели в словарь
- [x] Добавлена проверка длинны строки поля name в схеме.
- [x] Добавлена тестовая часть (функции tests() в deserialize.py и serialize.py) ,
      в которой есть сериализация и десериализация для единичного экземпляра и списка экземпляров.
- [x] Реализована замена поля с final_test на olympic в schema.py
      вывести словарь можно функцией tests() из serialize.py
    
