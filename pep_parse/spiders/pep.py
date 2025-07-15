import scrapy
from pep_parse.items import PepParseItem
from urllib.parse import urljoin

from pep_parse.constants import ALLOWED_DOMAINS, START_URL, SPIDER_NAME


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URL

    def parse(self, response):
        for pep in response.css('table.pep-zero-table tbody tr'):
            link = pep.css('a[href*="pep-"]::attr(href)').get()
            if link:
                yield response.follow(
                    urljoin(response.url, link),
                    callback=self.parse_pep
                )

    def parse_pep(self, response):
        pep_number = response.url.split('/')[-2].split('-')[-1]
        title = response.css('h1.page-title::text').get().strip()
        name = title.split(' - ', 1)[-1].strip()
        status = response.css(
            'dt:contains("Status") + dd abbr::text, dt:contains("Status") + dd::text'
        ).get().strip()
        yield PepParseItem(
            number=pep_number,
            name=name,
            status=status
        )
