"""
Стиль цитирования по American Psychological Association
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel, NewsPaperModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class APABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $title. $publishing_house."
        )

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
        )


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article ($access_date) $website $link"
        )

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APANewsPaperResource(BaseCitationStyle):
    """
    Форматирование для газеты.
    """

    data: NewsPaperModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($publishing_year, $publishing_date). $article_title. $news_title."
        )

    def substitute(self) -> str:
        logger.info('Форматирование газеты "%s" ...', self.data.article_title)

        return self.template.substitute(
            article_title=self.data.article_title,
            authors=self.data.authors,
            news_title=self.data.news_title,
            publishing_year=self.data.publishing_year,
            publishing_date=self.data.publishing_date
        )


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        InternetResourceModel.__name__: APAInternetResource,
        NewsPaperModel.__name__: APANewsPaperResource,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.
        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.
        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
