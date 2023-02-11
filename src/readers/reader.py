"""
Чтение исходного файла.
"""
from datetime import date
from typing import Type

import openpyxl
from openpyxl.workbook import Workbook

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    AbstractModel,
    RegulationModel,
    NewsPaperModel,
)
from logger import get_logger
from readers.base import BaseReader

logger = get_logger(__name__)


class BookReader(BaseReader):
    """
    Чтение модели книги.
    """

    @property
    def model(self) -> Type[BookModel]:
        return BookModel

    @property
    def sheet(self) -> str:
        return "Книга"

    @property
    def attributes(self) -> dict:
        return {
            "authors": {0: str},
            "title": {1: str},
            "edition": {2: str},
            "city": {3: str},
            "publishing_house": {4: str},
            "year": {5: int},
            "pages": {6: int},
        }


class InternetResourceReader(BaseReader):
    """
    Чтение модели интернет-ресурса.
    """

    @property
    def model(self) -> Type[InternetResourceModel]:
        return InternetResourceModel

    @property
    def sheet(self) -> str:
        return "Интернет-ресурс"

    @property
    def attributes(self) -> dict:
        return {
            "article": {0: str},
            "website": {1: str},
            "link": {2: str},
            "access_date": {3: date},
        }


class ArticlesCollectionReader(BaseReader):
    """
    Чтение модели сборника статей.
    """

    @property
    def model(self) -> Type[ArticlesCollectionModel]:
        return ArticlesCollectionModel

    @property
    def sheet(self) -> str:
        return "Статья из сборника"

    @property
    def attributes(self) -> dict:
        return {
            "authors": {0: str},
            "article_title": {1: str},
            "collection_title": {2: str},
            "city": {3: str},
            "publishing_house": {4: str},
            "year": {5: int},
            "pages": {6: str},
        }


class AbstractReader(BaseReader):
    """
    Чтение модели автореферата.
    """

    @property
    def model(self) -> Type[AbstractModel]:
        return AbstractModel

    @property
    def sheet(self) -> str:
        return "Автореферат"

    @property
    def attributes(self) -> dict:
        return {
            "author": {0: str},
            "abstract_title": {1: str},
            "author_status": {2: str},
            "science_field": {3: str},
            "specialty_code": {4: str},
            "city": {5: str},
            "year": {6: int},
            "pages": {7: str},
        }


class RegulationReader(BaseReader):
    """
    Чтение модели нормативного акта.
    """

    @property
    def model(self) -> Type[RegulationModel]:
        return RegulationModel

    @property
    def sheet(self) -> str:
        return " Закон, нормативный акт и т.п."

    @property
    def attributes(self) -> dict:
        return {
            "source": {0: str},
            "regulation_title": {1: str},
            "acceptance_date": {2: date},
            "regulation_id": {3: str},
            "publishing_source": {4: str},
            "publishing_year": {5: int},
            "publishing_source_id": {6: str},
            "publishing_article_id": {7: str},
            "modification_date": {8: date},
        }


class NewsPaperReader(BaseReader):
    """
    Чтение модели газеты.
    """

    @property
    def model(self) -> Type[NewsPaperModel]:
        return NewsPaperModel

    @property
    def sheet(self) -> str:
        return "Статья из газеты"

    @property
    def attributes(self) -> dict:
        return {
            "authors": {0: str},
            "article_title": {1: str},
            "news_title": {2: str},
            "publishing_year": {3: int},
            "publishing_date": {4: str},
            "publishing_number": {5: int},
        }


class SourcesReader:
    """
    Чтение из источника данных.
    """

    # зарегистрированные читатели
    readers = [
        BookReader,
        InternetResourceReader,
        ArticlesCollectionReader,
        AbstractReader,
        RegulationReader,
        NewsPaperReader,
    ]

    def __init__(self, path: str) -> None:
        """
        Конструктор.

        :param path: Путь к исходному файлу для чтения.
        """

        logger.info("Загрузка рабочей книги ...")
        self.workbook: Workbook = openpyxl.load_workbook(path)

    def read(self) -> list:
        """
        Чтение исходного файла.

        :return: Список прочитанных моделей (строк).
        """

        items = []
        for reader in self.readers:
            logger.info("Чтение %s ...", reader)
            items.extend(reader(self.workbook).read())  # type: ignore

        return items
