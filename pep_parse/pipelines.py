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
    def open_spider(self, spider):
        """Инициализация pipeline при запуске паука."""
        self.status_counts = defaultdict(int)
        self.results_dir = RESULTS_DIR

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
        filename = f'{self.results_dir}/status_summary_{timestamp}.csv'
        filepath = BASE_DIR / filename
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in sorted(self.status_counts.items()):
                writer.writerow([status, count])
            writer.writerow(['Total', total])
