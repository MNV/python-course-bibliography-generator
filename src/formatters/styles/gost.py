"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, AbstractModel, RegulationModel
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


class GOSTAbtract(BaseCitationStyle):
    """
    Форматирование для автореферата.
    """

    data: AbstractModel

    @property
    def template(self) -> Template:
        return Template(
            "$author $abstract_title: автореф. дис. ... $author_status $science_field наук: $specialty_code. $city, "
            "$year. $pages с."
        )

    def substitute(self) -> str:
        logger.info('Форматирование автореферата "%s" ...', self.data.abstract_title)

        return self.template.substitute(
            author=self.data.author,
            abstract_title=self.data.abstract_title,
            author_status=self.data.author_status,
            science_field=self.data.science_field,
            specialty_code=self.data.specialty_code,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )


class GOSTRegulation(BaseCitationStyle):
    """
    Форматирование для нормативного акта.
    """

    data: RegulationModel

    @property
    def template(self) -> Template:
        return Template(
            "$source \"$regulation_title\" от $acceptance_date № $regulation_id // $publishing_source. "
            "$publishing_year г. № $publishing_source_id. Ст. $publishing_article_id с изм. и допол. в ред. от "
            "$modification_date"
        )

    def substitute(self) -> str:
        logger.info('Форматирование нормативного акта "%s" ...', self.data.regulation_title)

        return self.template.substitute(
            regulation_title=self.data.regulation_title,
            source=self.data.source,
            publishing_source=self.data.publishing_source,
            regulation_id=self.data.regulation_id,
            acceptance_date=self.data.acceptance_date,
            publishing_year=self.data.publishing_year,
            publishing_source_id=self.data.publishing_source_id,
            publishing_article_id=self.data.publishing_article_id,
            modification_date=self.data.modification_date
        )


class GOSTCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        AbstractModel.__name__: GOSTAbtract,
        RegulationModel.__name__: GOSTRegulation
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
