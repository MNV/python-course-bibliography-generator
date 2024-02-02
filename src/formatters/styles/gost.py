"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    NewspaperArticleModel,
    DissertationModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


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


class GOSTNewspaperArticle(BaseCitationStyle):
    """
    Форматирование для статьи из газеты.
    """

    data: NewspaperArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $newspaper_title. – $year. - $date. - №$number."
        )

    def substitute(self) -> str:

        logger.info('Форматирование статьи из газеты "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            newspaper_title=self.data.newspaper_title,
            year=self.data.year,
            date=self.data.date,
            number=self.data.number,
        )


class GOSTDissertationModel(BaseCitationStyle):
    """
    Форматирование для диссертации.
    """

    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author $title: дис. ... $degree $science_field наук: $code $city $year. $page_count с."
        )

    def substitute(self) -> str:

        logger.info('Форматирование диссертации "%s" ...', self.data.title)

        return self.template.substitute(
            author=self.data.author,
            title=self.data.title,
            degree=self.data.degree,
            science_field=self.data.science_field,
            code=self.data.code,
            city=self.data.city,
            year=self.data.year,
            page_count=self.data.page_count,
        )


class GOSTCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        NewspaperArticleModel.__name__: GOSTNewspaperArticle,
        DissertationModel.__name__: GOSTDissertationModel,
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
