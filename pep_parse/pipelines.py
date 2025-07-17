import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.constants import RESULTS_DIR, TIME_FORMAT
from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    """Pipeline для обработки и анализа данных о PEP.

    Собирает статистику по статусам PEP и сохраняет результаты
    в CSV-файл.
    """

    def __init__(self):
        """Инициализация pipeline и создание директории для результатов."""
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(parents=True, exist_ok=True)
        self.status_counts = defaultdict(int)

    def open_spider(self, spider):
        """Подготовка к работе при запуске паука.

        Сбрасывает счетчик статусов перед началом обработки.
        """
        self.status_counts.clear()

    def process_item(self, item, spider):
        """Обработка каждого элемента PEP.

        Увеличивает счетчик для текущего статуса PEP.
        """
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Завершения работы паука.

        Формирует и сохраняет сводку со статусами в CSV-файл.
        Добавляет итоговую строку с общим количеством PEP.
        """
        total = sum(self.status_counts.values())
        timestamp = datetime.now().strftime(TIME_FORMAT)
        filename = f'status_summary_{timestamp}.csv'
        filepath = self.results_dir / filename
        data = [
            ['Статус', 'Количество'],
            *[(status, str(count)) for status, count in sorted(
                self.status_counts.items()
            )],
            ['Total', str(total)]
        ]
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
