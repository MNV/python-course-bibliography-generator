"""
Стиль цитирования по MLA
"""
from string import Template
from pydantic import BaseModel
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, DissertationModel, ArticleFromTheJournalModel
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
        return Template(
            "$authors. $title. $edition, $city: $publishing_house, $year"
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

        return f"{self.data.edition} изд." if self.data.edition else ""


class MLAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """
    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article. $website, $access_date, $link"
        )

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
            "$authors. $article_title. $collection_title. $city, $publishing_house, $year, с.$pages."
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
    

class MLADissertation(BaseCitationStyle):
    """
    Форматирование для диссертации.
    """
    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
           "$author. $title.$year. $city. $publisher_status $branch_of_sciences наук." 
        )

    def substitute(self) -> str:
        logger.info('Форматирование диссертаций "%s" ...', self.data.title)

        return self.template.substitute(
            author=self.data.author,
            title=self.data.title,
            publisher_status=self.data.publisher_status,
            branch_of_sciences=self.data.branch_of_sciences,
            speciality_code=self.data.speciality_code,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )
    

class MLAArticleFromTheJournal(BaseCitationStyle):
    """
    Форматирование для статьи из журнала.
    """
    data: ArticleFromTheJournalModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors. $article_title. $collection_title,($number_of_journal),$year,с.$pages."
        )

    def substitute(self) -> str:
        logger.info('Форматирование статьи из журнала "%s"...', self.data.article_title)

        return self.template.substitute(
            authors=self.data.authors,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            year=self.data.year,
            number_of_journal=self.data.number_of_journal,
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
        DissertationModel.__name__: MLADissertation,
        ArticleFromTheJournalModel.__name__: MLAArticleFromTheJournal,
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