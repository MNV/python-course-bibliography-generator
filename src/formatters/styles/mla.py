"""
Стиль цитирования по Modern Language Association 9th edition.
"""
from string import Template

from pydantic import BaseModel

from src.formatters.models import MLABookModel, MLAInternetResourceModel
from src.formatters.styles.base import BaseCitationStyle
from src.logger import get_logger

logger = get_logger(__name__)


class MLABook(BaseCitationStyle):
    """
    Форматирование для книг.
    """

    data: MLABookModel

    @property
    def template(self) -> Template:
        return Template(
            "$author_last_name, $author_first_name. $title. $edition$publisher, $year."
        )

    def substitute(self) -> str:
        logger.info('Форматирование книги MLA "%s" ...', self.data.title)

        return self.template.substitute(
            author_last_name=self.data.author_last_name,
            author_first_name=self.data.author_first_name,
            title=self.data.title,
            edition=self.get_edition(),
            publisher=self.data.publisher,
            year=self.data.year,
        )

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издании.

        :return: Информация об издании.
        """

        return f"{self.data.edition} ed. " if self.data.edition else ""


class MLAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов MLA.
    """

    data: MLAInternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$author_last_name, $author_first_name. “$title” $website, $publication_date, $url."
        )

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса MLA "%s" ...', self.data.title)

        return self.template.substitute(
            author_last_name=self.data.author_last_name,
            author_first_name=self.data.author_first_name,
            title=self.data.title,
            website=self.data.website,
            publication_date=self.data.publication_date,
            url=self.data.url,
        )


class MLACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        MLABookModel.__name__: MLABook,
        MLAInternetResourceModel.__name__: MLAInternetResource
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
