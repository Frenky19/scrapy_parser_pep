from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import ALLOWED_DOMAINS, START_URL, SPIDER_NAME


class PepSpider(scrapy.Spider):
    """Парсер документов PEP (Python Enhancement Proposals).

    Собирает данные со страницы https://peps.python.org/numerical/:
    - Номер PEP
    - Название
    - Статус документа

    Формирует Items для последующей обработки в пайплайне.
    """
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URL

    def parse(self, response):
        """Основной метод парсинга списка PEP.

        Обрабатывает страницу с таблицей PEP, собирает ссылки на все документы
        PEP и формирует запросы для их обработки.
        """
        for pep in response.css('table.pep-zero-table tbody tr'):
            link = pep.css('a[href*="pep-"]::attr(href)').get()
            if link:
                yield response.follow(
                    urljoin(response.url, link),
                    callback=self.parse_pep
                )

    def parse_pep(self, response):
        """Парсит страницу отдельного документа PEP.

        Извлекает номер, название и статус PEP. Формирует Item
        с собранными данными для последующей обработки.
        """
        pep_number = response.url.split('/')[-2].split('-')[-1]
        title = response.css('h1.page-title::text').get().strip()
        name = title.split(' - ', 1)[-1].strip()
        status = response.css(
            'dt:contains("Status") + dd abbr::text'
        ).get().strip()
        yield PepParseItem(
            number=pep_number,
            name=name,
            status=status
        )
