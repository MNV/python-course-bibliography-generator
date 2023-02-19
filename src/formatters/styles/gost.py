"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from src.formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ArticleMagazineModel, \
    LawModel
from src.formatters.styles.base import BaseCitationStyle
from src.logger import get_logger

logger = get_logger(__name__)


class GOSTBook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title. – $edition$city: $publishing_house, $year. – $pages с."
        )

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class GOSTInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article // $website URL: $link (дата обращения: $access_date)."
        )

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class GOSTCollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $collection_title. – $city: $publishing_house, $year. – С. $pages."
        )

    def substitute(self) -> str:
        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTMagazineArticle(BaseCitationStyle):
    """
    Форматирование для статьи из журнала.
    """

    data: ArticleMagazineModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $magazine_title. – $year. – №$number. – С. $pages."
        )

    def substitute(self) -> str:
        logger.info('Форматирование статьи из журнала "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            magazine_title=self.data.magazine_title,
            year=self.data.year,
            number=self.data.number,
            pages=self.data.pages,
        )


class GOSTLaw(BaseCitationStyle):
    """
    Форматирование для закона, нормативного актa и т.п.
    """

    data: LawModel

    @property
    def template(self) -> Template:
        return Template(
            "$type \"$law_title\" от $passing_date № $number // $source. - $source_year г. - № $source_number. - Ст. "
            "$article_number с изм. и допол. в ред. от $start_date."
        )

    def substitute(self) -> str:
        logger.info('Форматирование закона, нормативного актa и т.п. "%s" ...', self.data.law_title)

        return self.template.substitute(
            type=self.data.type,
            law_title=self.data.law_title,
            passing_date=self.data.passing_date,
            number=self.data.number,
            source=self.data.source,
            source_year=self.data.source_year,
            source_number=self.data.source_number,
            article_number=self.data.article_number,
            start_date=self.data.start_date,
        )


class GOSTCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        ArticleMagazineModel.__name__: GOSTMagazineArticle,
        LawModel.__name__: GOSTLaw,
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
