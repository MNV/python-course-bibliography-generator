"""
Стиль цитирования по American Psychological Association.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import InternetResourceModel, MagazineArticleModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template("/i/$article/i/. ($access_date). $website. $link")

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APAMagazineArticle(BaseCitationStyle):
    """
    Форматирование для статьи из журнала.
    """

    data: MagazineArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $article_title. /i/$magazine_title/i/, $volume, $pages."
        )

    def substitute(self) -> str:

        logger.info('Форматирование статьи из журнала "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            magazine_title=self.data.magazine_title,
            year=self.data.year,
            volume=self.data.volume,
            pages=self.data.pages,
        )


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        MagazineArticleModel.__name__: APAMagazineArticle,
        InternetResourceModel.__name__: APAInternetResource,
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
