import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.constants import RESULTS_DIR, TIME_FORMAT
from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)
        self.results_dir = RESULTS_DIR

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
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
