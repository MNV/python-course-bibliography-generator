"""
Стиль цитирования по ГОСТ Р 7.0.5-2008.
"""
from string import Template

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    NormativeActModel,
    JournalArticleModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class GOSTJournalArticle(BaseCitationStyle):
    """
    Форматирование для статей из журналов.
    """

    data: JournalArticleModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors $article_title // $journal_name. $publication_year. № $journal_number, С. $pages."
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


class GOSTNormativeAct(BaseCitationStyle):
    """
    Форматирование для законов и нормативных актов.
    """

    data: NormativeActModel

    @property
    def template(self) -> Template:
        return Template(
            "$title : $type от $adoption_date № $act_numer // $source. $publication_year. "
            "№$source_number. Ст. $article_number. $revision."
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


class GOSTCitationFormatter(BaseCitationFormatter):
    """
    Класс для итогового форматирования списка источников по ГОСТ.
    """

    formatters_map = {
        BookModel.__name__: GOSTBook,
        InternetResourceModel.__name__: GOSTInternetResource,
        ArticlesCollectionModel.__name__: GOSTCollectionArticle,
        NormativeActModel.__name__: GOSTNormativeAct,
        JournalArticleModel.__name__: GOSTJournalArticle,
    }

