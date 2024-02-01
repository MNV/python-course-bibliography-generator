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
    RegulatoryActModel,
    ArticleModel,
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


class ArticleReader(BaseReader):
    """
    Чтение модели статей.
    """

    @property
    def model(self) -> Type[ArticleModel]:
        return ArticleModel

    @property
    def sheet(self) -> str:
        return "Статья из журнала"

    @property
    def attributes(self) -> dict:
        return {
            "authors": {0: str},
            "title": {1: str},
            "journal_name": {2: str},
            "year": {3: int},
            "No": {4: int},
            "pages": {5: str},
        }


class RegulatoryActReader(BaseReader):
    """
    Чтение модели нормативного акта.
    """

    @property
    def model(self) -> Type[RegulatoryActModel]:
        return RegulatoryActModel

    @property
    def sheet(self) -> str:
        return "Закон, нормативный акт и т.п."

    @property
    def attributes(self) -> dict:
        return {
            "act_type": {0: str},
            "full_name": {1: str},
            "acception_date": {2: date},
            "act_No": {3: str},
            "publishing_source": {4: str},
            "year": {5: int},
            "source_No": {6: int},
            "article_No": {7: int},
            "amended_from": {8: date},
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


class SourcesReader:
    """
    Чтение из источника данных.
    """

    # зарегистрированные читатели
    readers = [
        BookReader,
        InternetResourceReader,
        ArticlesCollectionReader,
        RegulatoryActReader,
        ArticleReader,
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
