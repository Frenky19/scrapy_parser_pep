from pathlib import Path

from pep_parse.constants import PROJECT_NAME, RESULTS_DIR

BOT_NAME = PROJECT_NAME

SPIDER_MODULES = [f'{PROJECT_NAME}.spiders']
NEWSPIDER_MODULE = f'{PROJECT_NAME}.spiders'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
