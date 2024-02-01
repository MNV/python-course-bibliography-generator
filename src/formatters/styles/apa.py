"""
Стиль цитирования APA 7.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import (
    InternetResourceModel,
    JournalArticleModel,
    NormativeActModel,
    BookModel,
    ArticlesCollectionModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class APAJournalArticle(BaseCitationStyle):
    """
    Форматирование для статей из журналов.
    """

    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($publication_year). $article_title. $journal_name, $journal_number, $pages."
        )

    def substitute(self) -> str:

        logger.info(
            'Форматирование статьи из журнала "%s" ...', self.data.article_title
        )
        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            journal_name=self.data.journal_name,
            publication_year=self.data.publication_year,
            journal_number=self.data.journal_number,
            pages=self.data.pages,
        )


class APANormativeAct(BaseCitationStyle):
    """
    Форматирование для законов и нормативных актов.
    """

    data: NormativeActModel

    @property
    def template(self) -> Template:
        return Template(
            "$title, $type No. $act_numer, Stat. $article_number ($adoption_date)."
        )

    def substitute(self) -> str:

        logger.info('Форматирование нормативного акта "%s" ...', self.data.title)
        return self.template.substitute(
            type=self.data.type,
            title=self.data.title,
            adoption_date=self.data.adoption_date,
            act_numer=self.data.act_numer,
            source=self.data.source,
            publication_year=self.data.publication_year,
            source_number=self.data.source_number,
            article_number=self.data.article_number,
            revision=self.get_revision_date(),
        )

    def get_revision_date(self) -> str:
        """
        Получение отформатированной информации о дате редактуры.

        :return: Информация о дате редакции.
        """
        return f"в ред. от {self.data.revision}" if self.data.revision else ""


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article. (n.d.). $website. Retrieved $access_date, from $link"
        )

    def substitute(self) -> str:

        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $title. $publishing_house.")

    def substitute(self) -> str:

        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
        )


class APACollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $article_title. $collection_title, $pages.")

    def substitute(self) -> str:

        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            year=self.data.year,
            pages=self.data.pages,
        )


class APACitationFormatter:
    """
    Класс для итогового форматирования списка источников по APA 7.
    """

    formatters_map = {
        InternetResourceModel.__name__: APAInternetResource,
        JournalArticleModel.__name__: APAJournalArticle,
        BookModel.__name__: APABook,
        ArticlesCollectionModel.__name__: APACollectionArticle,
        NormativeActModel.__name__: APANormativeAct,
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
