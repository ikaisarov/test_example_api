# Тестовый проект для https://reqres.in/api

#### Стэк
- язык программирования - [Python](https://www.python.org/downloads/)
- тестовый фреймворк - [pytest](https://docs.pytest.org/en/latest/)
- отчеты - [allure](https://docs.qameta.io/allure/)

#### Структура
```bash
.
├── core
│   ├── api                 # описание api клиента
│   ├── base                # базовые хелперы 
│   ├── enums               # enum
│   ├── model               # описание моделей для pydantic
│   ├── randomizer          # генерация различных рандомных данных
│   ├── utils               # утилиты и дата-билдеры
├── tests
│   └── test_*.py           # тесты
├── .gitignore              # список игнорируемых гитом файлов, папок    
├── conftest.py             # фикстуры    
├── pytest.ini              # конфигурация pytest  
└── requirements.txt        # подключение внешних библиотек
```

## Установка
1. Клонируем проект
   <br>`git clone https://github.com/ikaisarov/test_example_api.git`
2. В проекте устанавливаем виртуальное окружение [virtualenv](https://virtualenv.pypa.io/en/latest/) и активируем его:
<br> Windows `venv\Scripts\activate.bat`
<br> MacOS/Linux `source venv/bin/activate`
3. Устанавливаем все зависимости из файла `requirements.txt`
<br> `pip install -r requirements.txt`
4. Скачать пакет [allure](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.22.1/allure-commandline-2.22.1.zip). Архив распаковать в каталоге проекта в отдельной папке: allure-cli

## Запуск тестов
Выполнить команду:
<br>`pytest`

## Сформировать отчет:
Выполнить команду:
<br>`allure-cli\bin\allure serve .\allure-results`
