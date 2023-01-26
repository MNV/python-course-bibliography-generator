"""
Стиль цитирования по APA 7th.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, JournalArticleModel, DissertationModel
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

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """

        return f"{self.data.edition} изд. – " if self.data.edition else ""


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article (n.d.) $website $link"
        )

    def substitute(self) -> str:

        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
        )


class APACollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $article_title. $collection_title, $pages."
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
class APAJournalArticle(BaseCitationStyle):
    """
    Форматирование для статьи из журнала.
    """

    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $article_title. $journal_title, $journal_number, $pages."
        )

    def substitute(self) -> str:

        logger.info('Форматирование статей из журнала "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            journal_title=self.data.journal_title,
            year=self.data.year,
            journal_number = self.data.journal_number,
            pages=self.data.pages,
        )
class APADissertation(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $desertation_title [$canddoc диссиртация]"
        )

    def substitute(self) -> str:

        logger.info('Форматирование диссертации "%s" ...', self.data.desertation_title)

        return self.template.substitute(
            authors=self.data.authors,
            desertation_title=self.data.desertation_title,
            canddoc=self.data.canddoc,
            sience=self.data.sience,
            code=self.data.code,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )
class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        InternetResourceModel.__name__: APAInternetResource,
        ArticlesCollectionModel.__name__: APACollectionArticle,
        DissertationModel.__name__: APADissertation,
        JournalArticleModel.__name__: APAJournalArticle,
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