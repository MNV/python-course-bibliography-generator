"""
Стиль цитирования по MLA.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    RegulatoryActModel,
    ArticleModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class MLABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors $title. $edition$city: $publishing_house, $year.")

    def substitute(self) -> str:

        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.data.authors,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """
        if self.data.edition:
            edition = int(self.data.edition.split("-")[0])
            res = f"{edition}th"
            if 10 <= edition % 100 <= 19:
                res = f"{edition}th"
            elif edition % 10 == 1:
                res = f"{edition}st"
            elif edition % 10 == 2:
                res = f"{edition}nd"
            elif edition % 10 == 3:
                res = f"{edition}rd"
            return f"{res} ed., "
        return ""


class MLAArticle(BaseCitationStyle):
    """
    Форматирование для статьи журнала.
    """

    data: ArticleModel

    @property
    def template(self) -> Template:
        return Template('$authors "$title." $journal_name, no. $No, $year, pp. $pages.')

    def substitute(self) -> str:

        logger.info('Форматирование статьи журнала "%s" ...', self.data.title)

        authors = self.data.authors.split(",")
        res_authors = self.data.authors
        if len(authors) == 2:
            res_authors = f"{authors[0]} and {authors[1]}"
        elif len(authors) >= 3:
            res_authors = f"{authors[0]}, et al."
        return self.template.substitute(
            authors=res_authors,
            title=self.data.title,
            journal_name=self.data.journal_name,
            year=self.data.year,
            No=self.data.No,
            pages=self.data.pages,
        )


class MLARegulatoryAct(BaseCitationStyle):
    """
    Форматирование для нормативного акта.
    """

    data: RegulatoryActModel

    @property
    def template(self) -> Template:
        return Template(
            "$full_name. Pub L. $act_No. $acception_date. $publishing_source."
        )

    def substitute(self) -> str:

        logger.info('Форматирование нормативного акта "%s" ...', self.data.full_name)

        return self.template.substitute(
            full_name=self.data.full_name,
            acception_date=self.data.acception_date,
            act_No=self.data.act_No,
            publishing_source=self.data.publishing_source,
        )


class MLAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template('"$article." $website, $link. Accessed $access_date.')

    def substitute(self) -> str:

        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class MLACollectionArticle(BaseCitationStyle):
    """
    Форматирование для статьи из сборника.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            '$authors "$article_title." $collection_title, $publishing_house, $year, pp. $pages.'
        )

    def substitute(self) -> str:

        logger.info('Форматирование сборника статей "%s" ...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
            pages=self.data.pages,
        )


class MLACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: MLABook,
        InternetResourceModel.__name__: MLAInternetResource,
        ArticlesCollectionModel.__name__: MLACollectionArticle,
        RegulatoryActModel.__name__: MLARegulatoryAct,
        ArticleModel.__name__: MLAArticle,
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
