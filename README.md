# Python Documentation Parser with Scrapy
Этот проект представляет собой парсер для сбора информации о PEP (Python Enhancement Proposals) с официального сайта Python. Парсер собирает данные о каждом PEP и формирует два отчёта в формате CSV.

# Особенности

- Собирает данные со страницы https://peps.python.org/numerical/
- Формирует два отчёта:
  - Полный список PEP с номерами, названиями и статусами
  - Сводку по статусам PEP с подсчётом количества и общим итогом
- Автоматически создаёт директорию results для сохранения отчётов
- Генерирует файлы с уникальными именами, содержащими дату и время создания

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/Frenky19/scrapy_parser_pep.git
cd scrapy_parser_pep
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv .venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

## Использование

1. Выполните команду:

```
scrapy crawl pep
```

2. После выполнения в директории results будут созданы два файла:

- pep_<дата_время>.csv - полный список PEP

- status_summary_<дата_время>.csv - сводка по статусам PEP

### Доступные режимы:

- whats-new: Нововведения в Python
- latest-versions: Последние версии Python
- download: Скачать документацию PDF
- pep: Анализ статусов PEP

### Опции:

-c, --clear-cache: Очистить кеш перед выполнением

-o {pretty,file}, --output {pretty,file}: Формат вывода результатов

### Примеры команд:

1. Получить информацию о нововведениях с красивым выводом:

```
python main.py whats-new -o pretty
```

2. Проанализировать статусы PEP и сохранить в файл:

```
python main.py pep -o file
```

3. Получить информацию о последних версиях Python, очистив кеш:

```
python main.py latest-versions -c
```


## Структура проекта

### Файл со списком PEP (pep_*.csv)

Содержит три колонки:

- number - номер PEP

- name - название PEP

- status - текущий статус

Пример:

```
number,name,status
0102,PEP 102 – Doing Python Micro Releases,Superseded
0020,PEP 20 – The Zen of Python,Active
...
```

### Файл со сводкой статусов (status_summary_*.csv)

Содержит две колонки:

- Статус - статус PEP

- Количество - количество PEP с этим статусом (Последняя строка содержит общее количество PEP)

Пример:

```
Статус,Количество
Active,35
Accepted,21
...
Total,692
```

## Технические детали

### Компоненты проекта

Spider (pep.py):

- Обрабатывает страницу с таблицей PEP

- Собирает ссылки на все документы PEP

- Парсит каждую страницу PEP для извлечения данных

Item (items.py):

- Определяет структуру данных для каждого PEP:

  - number - номер PEP

  - name - название PEP

  - status - статус документа

Pipeline (pipelines.py):

- Собирает статистику по статусам

- Формирует итоговый отчёт со сводкой по  статусам

- Сохраняет отчёт в CSV-файл

## Автор  
[Андрей Головушкин / Andrey Golovushkin](https://github.com/Frenky19)
