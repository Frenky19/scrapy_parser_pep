"""Содержит константы, используемые в проекте парсера PEP.

Константы:
    TIME_FORMAT: Формат временной метки для именования файлов
    START_URL: Стартовый URL для парсера
    ALLOWED_DOMAINS: Домены, разрешенные для парсинга
    SPIDER_NAME: Имя паука Scrapy
    RESULTS_DIR: Директория для сохранения результатов
"""

# Формат временной метки для именования файлов результатов

TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# Стартовый URL для парсера

START_URL = ['https://peps.python.org/numerical/']

# Домены, разрешенные для парсинга

ALLOWED_DOMAINS = ['peps.python.org']

# Имя паука Scrapy

SPIDER_NAME = 'pep'

# Директория для сохранения результатов работы парсера
RESULTS_DIR = 'results'
