"""
Стиль цитирования по APA 7.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, RegulatoryActModel, ArticleModel
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
            "$authors. ($year). $title$edition. $publishing_house."
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
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издательстве.

        :return: Информация об издательстве.
        """
        if self.data.edition:
            ed = int(self.data.edition.split("-")[0])
            res = f"{ed}th"
            if  10 <= ed % 100 <=19:
                res = f"{ed}th"
            elif ed % 10 == 1:         
                res = f"{ed}st"       
            elif ed % 10 == 2:     
                res = f"{ed}nd"           
            elif ed % 10 == 3:      
                res = f"{ed}rd"         
            return f" ({res} ed.)"
        return ""


class APAArticle(BaseCitationStyle):
    """
    Форматирование для статьи журнала.
    """

    data: ArticleModel

    @property
    def template(self) -> Template:
        return Template(
            '$authors ($year). $title. $journal_name. ($No), $pages.'
        )

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


class APARegulatoryAct(BaseCitationStyle):
    """
    Форматирование для нормативного акта.
    """

    data: RegulatoryActModel

    @property
    def template(self) -> Template:
        return Template(
            '$full_name, $act_No $publishing_source. § $article_No ($year).'
        )

    def substitute(self) -> str:

        logger.info('Форматирование нормативного акта "%s" ...', self.data.full_name)

        return self.template.substitute(
            full_name=self.data.full_name,
            publishing_source=self.data.publishing_source,
            act_No=self.data.act_No,
            article_No=self.data.article_No,
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
            '$article. $website. (n.d.). $link'
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
            '$authors ($year). $article_title, $collection_title. (pp. $pages). $publishing_house.'
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


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        InternetResourceModel.__name__: APAInternetResource,
        ArticlesCollectionModel.__name__: APACollectionArticle,
        RegulatoryActModel.__name__: APARegulatoryAct,
        ArticleModel.__name__: APAArticle,
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
