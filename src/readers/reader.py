"""
Чтение исходного файла.
"""
from datetime import date
from typing import Type

import openpyxl
from openpyxl.workbook import Workbook

from src.formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ArticleMagazineModel, \
    LawModel, MLABookModel, MLAInternetResourceModel
from src.logger import get_logger
from src.readers.base import BaseReader

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


class ArticleMagazineReader(BaseReader):
    """
    Чтение модели сборника из журнала.
    """

    @property
    def model(self) -> Type[ArticleMagazineModel]:
        return ArticleMagazineModel

    @property
    def sheet(self) -> str:
        return "Статья из журнала"

    @property
    def attributes(self) -> dict:
        return {
            "authors": {0: str},
            "article_title": {1: str},
            "magazine_title": {2: str},
            "year": {3: int},
            "number": {4: int},
            "pages": {5: str},
        }


class LawReader(BaseReader):
    """
    Чтение модели закона, нормативного актa и т.п..
    """

    @property
    def model(self) -> Type[LawModel]:
        return LawModel

    @property
    def sheet(self) -> str:
        return " Закон, нормативный акт и т.п."

    @property
    def attributes(self) -> dict:
        return {
            "type": {0: str},
            "law_title": {1: str},
            "passing_date": {2: date},
            "number": {3: str},
            "source": {4: str},
            "source_year": {5: int},
            "source_number": {6: int},
            "article_number": {7: int},
            "start_date": {8: date},
        }


class MLABookReader(BaseReader):
    """
    Чтение модели книги MLA.
    """

    @property
    def model(self) -> Type[MLABookModel]:
        return MLABookModel

    @property
    def sheet(self) -> str:
        return "Книга MLA"

    @property
    def attributes(self) -> dict:
        return {
            "author_last_name": {0: str},
            "author_first_name": {1: str},
            "title": {2: str},
            "edition": {3: str},
            "publisher": {4: str},
            "year": {5: int},
        }


class MLAInternetResourceReader(BaseReader):
    """
    Чтение модели интернес-ресурса MLA.
    """

    @property
    def model(self) -> Type[MLAInternetResourceModel]:
        return MLAInternetResourceModel

    @property
    def sheet(self) -> str:
        return "Интернет-ресурс MLA"

    @property
    def attributes(self) -> dict:
        return {
            "author_last_name": {0: str},
            "author_first_name": {1: str},
            "title": {2: str},
            "website": {3: str},
            "publication_date": {4: str},
            "url": {5: str},
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
        ArticleMagazineReader,
        LawReader,
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


class MLASourcesReader:
    """
    Чтение из источника данных.
    """

    # зарегистрированные читатели
    readers = [
        MLABookReader,
        MLAInternetResourceReader,
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

