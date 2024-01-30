"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, RegulatoryActModel, ArticleModel
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


class GOSTArticle(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: ArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $title // $journal_name. $year. №$No. С. $pages."
        )

    @property
    def template_many_authors(self) -> Template:
        return Template(
            "$title / $main_author [и др.] // $journal_name. $year. №$No. С. $pages."
        )

    def substitute(self) -> str:

        logger.info('Форматирование статьи журнала "%s" ...', self.data.title)

        authors = self.data.authors.split(",")
        if len(authors) >=4:
            return self.template_many_authors.substitute(
                title=self.data.title,
                main_author=authors[0],
                journal_name=self.data.journal_name,
                year=self.data.year,
                No=self.data.No,
                pages=self.data.pages,
            )
        else: 
            return self.template.substitute(
                authors=self.data.authors,
                title=self.data.title,
                journal_name=self.data.journal_name,
                year=self.data.year,
                No=self.data.No,
                pages=self.data.pages,
        )


class GOSTRegulatoryAct(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: RegulatoryActModel

    @property
    def template(self) -> Template:
        return Template(
            '$act_type "$full_name" от $acception_date №$act_No // $publishing_source, $year. – №$source_No – Ст. $article_No с изм. и допол. в ред. от $amended_from.'
        )

    def substitute(self) -> str:

        logger.info('Форматирование нормативного акта "%s" ...', self.data.full_name)

        return self.template.substitute(
            act_type=self.data.act_type,
            full_name=self.data.full_name,
            acception_date=self.data.acception_date,
            act_No=self.data.act_No,
            publishing_source=self.data.publishing_source,
            year=self.data.year,
            source_No=self.data.source_No,
            article_No=self.data.article_No,
            amended_from=self.data.amended_from,
        )


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


class GOSTCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        RegulatoryActModel.__name__: GOSTRegulatoryAct,
        ArticleModel.__name__: GOSTArticle,
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
