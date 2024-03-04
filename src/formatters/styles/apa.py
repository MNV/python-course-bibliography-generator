""" Стиль цитирования по APA. """
from string import Template

from pydantic import BaseModel

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    AbstractModel,
)
from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class APABookFormatter(BaseCitationStyle):
    """
    Форматирование для книг в стиле APA.
    """

    data: BookModel

    @property
    def template(self) -> Template:
        return Template("$authors ($year). $title. $edition. $city: $publishing_house.")

    def substitute(self) -> str:
        """
        Замена переменных в шаблоне источника.

        :return: Отформатированная строка источника.
        """

        logger.info('Форматирование книги "%s" в стиле APA...', self.data.title)

        return self.template.substitute(
            authors=self.get_authors(),
            year=self.data.year,
            title=self.data.title,
            edition=self.get_edition(),
            city=self.data.city,
            publishing_house=self.data.publishing_house,
        )

    def get_authors(self) -> str:
        """
        Получение списка авторов в формате APA.

        :return: Отформатированный список авторов.
        """
        authors = self.data.authors.split(
            ", "
        )  # Предполагая, что имена авторов разделены запятой
        formatted_authors = []
        for author in authors:
            # Разбиваем полное имя автора на фамилию и инициалы
            author_parts = author.split(" ")
            # Если есть хотя бы фамилия и одна инициала
            if len(author_parts) >= 2:
                # Форматируем фамилию, инициалы и точку
                formatted_author = (
                    author_parts[0]
                    + " "
                    + " ".join([initial[0] + "." for initial in author_parts[1:]])
                )
                formatted_authors.append(formatted_author)
            else:
                # В случае, если в имени только одно слово (без инициалов)
                formatted_authors.append(author)
        # Объединяем отформатированных авторов через запятую и пробел
        if len(formatted_authors) == 1:
            return formatted_authors[0]
        if len(formatted_authors) == 2:
            return formatted_authors[0] + " & " + formatted_authors[1]
        else:
            # Если авторов больше двух, добавляем "и др."
            return formatted_authors[0] + " et al."

    def get_edition(self) -> str:
        """
        Получение отформатированной информации об издании.

        :return: Информация об издании.
        """
        return f"({self.data.edition} изд.)" if self.data.edition else ""


class APAInternetResourceFormatter(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов в стиле APA.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template(
            "$article (б. д.). $website URL: $link (дата обращения: $access_date)."
        )

    def substitute(self) -> str:
        """
        Замена переменных в шаблоне источника.

        :return: Отформатированная строка источника.
        """

        logger.info(
            'Форматирование интернет-ресурса "%s" в стиле APA...', self.data.article
        )

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APACollectionArticleFormatter(BaseCitationStyle):
    """
    Форматирование для статьи из сборника в стиле APA.
    """

    data: ArticlesCollectionModel

    @property
    def template(self) -> Template:
        return Template(
            "$authors ($year). $article_title. $collection_title (pp. $pages). $city: $publishing_house."
        )

    def substitute(self) -> str:
        """
        Замена переменных в шаблоне источника.

        :return: Отформатированная строка источника.
        """

        logger.info(
            'Форматирование статьи из сборника "%s" в стиле APA...',
            self.data.article_title,
        )

        return self.template.substitute(
            authors=self.get_authors(),
            year=self.data.year,
            article_title=self.data.article_title,
            collection_title=self.data.collection_title,
            pages=self.data.pages,
            city=self.data.city,
            publishing_house=self.data.publishing_house,
        )

    def get_authors(self) -> str:
        """
        Получение списка авторов в формате APA.

        :return: Отформатированный список авторов.
        """
        authors = self.data.authors.split(
            ", "
        )  # Предполагая, что имена авторов разделены запятой
        formatted_authors = []
        for author in authors:
            # Разбиваем полное имя автора на фамилию и инициалы
            author_parts = author.split(" ")
            # Если есть хотя бы фамилия и одна инициала
            if len(author_parts) >= 2:
                # Форматируем фамилию, инициалы и точку
                formatted_author = (
                    author_parts[0]
                    + " "
                    + " ".join([initial[0] + "." for initial in author_parts[1:]])
                )
                formatted_authors.append(formatted_author)
            else:
                # В случае, если в имени только одно слово (без инициалов)
                formatted_authors.append(author)
        # Объединяем отформатированных авторов через запятую и пробел
        if len(formatted_authors) == 1:
            return formatted_authors[0]
        if len(formatted_authors) == 2:
            return formatted_authors[0] + " & " + formatted_authors[1]
        else:
            # Если авторов больше двух, добавляем "и др."
            return formatted_authors[0] + " et al."


class APADissertationFormatter(BaseCitationStyle):
    """
    Форматирование для диссертаций в стиле APA.
    """

    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author. ($year). $title ($degree) [Диссертация]. $branch, $speciality_code. $city"
        )

    def substitute(self) -> str:
        return self.template.substitute(
            author=self.data.author,
            year=self.data.year,
            title=self.data.title,
            degree=self.data.degree,
            branch=self.data.branch,
            speciality_code=self.data.speciality_code,
            city=self.data.city,
        )


class APAAbstractFormatter(BaseCitationStyle):
    """
    Форматирование для автореферата в стиле APA.
    """

    data: AbstractModel

    @property
    def template(self) -> Template:
        return Template(
            "$author. ($year). $title ($degree) [Автореферат]. $branch, $speciality_code. $city"
        )

    def substitute(self) -> str:
        return self.template.substitute(
            author=self.data.author,
            year=self.data.year,
            title=self.data.title,
            degree=self.data.degree,
            branch=self.data.branch,
            speciality_code=self.data.speciality_code,
            city=self.data.city,
        )


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        BookModel.__name__: APABookFormatter,
        InternetResourceModel.__name__: APAInternetResourceFormatter,
        ArticlesCollectionModel.__name__: APACollectionArticleFormatter,
        DissertationModel.__name__: APADissertationFormatter,
        AbstractModel.__name__: APAAbstractFormatter,
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
