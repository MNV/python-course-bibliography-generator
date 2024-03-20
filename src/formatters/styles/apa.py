"""
Стиль цитирования по American Psychological Association
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class Book_APA(BaseCitationStyle):
    """
    Форматирование Книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $title $edition. $publishing_house.")

    def substitute(self) -> str:

        logger.info('Форматирование Книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.publication_city,
            publishing_house=self.data.publishing_house,
            year=self.data.publication_year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение информации об издательстве.
        :return: Информация об издательстве.
        """

        return f"({self.data.edition} изд.)" if self.data.edition else ""


class InternetResource_APA(BaseCitationStyle):
    """
    Форматирование Интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article. (n.d.). $website. Retrieved $access_date, from $link"
        )

    def substitute(self) -> str:

        logger.info('Форматирование Интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class Formatter_APA:
    """
    Класс для форматирования списка источников по стандартам APA.
    """

    formatters_map = {
        BookModel.__name__: Book_APA,
        InternetResourceModel.__name__: InternetResource_APA,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор для форматирования.
        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__(model)))

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.
        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)