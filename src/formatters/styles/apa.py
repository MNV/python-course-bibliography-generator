"""
Стиль цитирования APA.
"""
from string import Template

from formatters.models import (
    InternetResourceModel,
    JournalArticleModel,
)
from formatters.base import BaseCitationFormatter
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


class APACitationFormatter(BaseCitationFormatter):
    """
    Класс для итогового форматирования списка источников по APA 7.
    """

    formatters_map = {
        InternetResourceModel.__name__: APAInternetResource,
        JournalArticleModel.__name__: APAJournalArticle,
    }
