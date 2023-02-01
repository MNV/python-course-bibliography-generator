"""
Стиль цитирования по American Psychological Association.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import BookModel, InternetResourceModel
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
        return Template("$authors ($year). /i/$title./i/ $publishing_house.")

    def substitute(self) -> str:
        logger.info('Форматирование книги "%s" ...', self.data.title)

        return self.template.substitute(
            authors=self.get_authors(),
            title=self.data.title,
            publishing_house=self.data.publishing_house,
            year=self.data.year,
        )

    def get_authors(self) -> str:
        """
        Получение отформатированной информации об авторах.

        :return: Информация об авторах.
        """
        authors = self.data.authors.split(",")
        result = ""
        if len(authors) > 1:
            for author in authors:
                if author in authors[-1]:
                    result += f"{author}"
                else:
                    result += f"{author} &"
        else:
            result = self.data.authors
        return result


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template("$website. ($access_date). /i/$article./i/ $website. $link")

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABook,
        InternetResourceModel.__name__: APAInternetResource,
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
