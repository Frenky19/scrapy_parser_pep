import scrapy


class PepParseItem(scrapy.Item):
    """Item для хранения данных о документах PEP.

    Содержит три основных поля:
    - number: номер документа PEP
    - name: название документа PEP
    - status: текущий статус документа
    """
    number = scrapy.Field(doc='Номер документа PEP.')
    name = scrapy.Field(doc='Название документа PEP.')
    status = scrapy.Field(doc='Текущий статус документа.')
