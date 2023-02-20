"""
Тестирование функций чтения данных из источника.
"""
from typing import Any

import pytest

from src.formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ArticleMagazineModel, \
    LawModel, MLABookModel, MLAInternetResourceModel
from src.readers.reader import (
    BookReader,
    SourcesReader,
    InternetResourceReader,
    ArticlesCollectionReader,
    ArticleMagazineReader,
    LawReader,
    MLABookReader,
    MLAInternetResourceReader
)
from src.settings import TEMPLATE_FILE_PATH


class TestReaders:
    """
    Тестирование функций чтения данных из источника.
    """

    @pytest.fixture
    def workbook(self) -> Any:
        """
         Получение объекта тестовой рабочей книги.
        :return:
        """

        return SourcesReader(TEMPLATE_FILE_PATH).workbook

    def test_book(self, workbook: Any) -> None:
        """
        Тестирование чтения книги.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = BookReader(workbook).read()

        assert len(models) == 4
        model = models[0]

        model_type = BookModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.title == "Наука как искусство"
        assert model.edition == "3-е"
        assert model.city == "СПб."
        assert model.publishing_house == "Просвещение"
        assert model.year == 2020
        assert model.pages == 999

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 7

    def test_internet_resource(self, workbook: Any) -> None:
        """
        Тестирование чтения интернет-ресурса.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = InternetResourceReader(workbook).read()

        assert len(models) == 3
        model = models[0]

        model_type = InternetResourceModel

        assert isinstance(model, model_type)
        assert model.article == "Наука как искусство"
        assert model.website == "Ведомости"
        assert model.link == "https://www.vedomosti.ru"
        assert model.access_date == "01.01.2021"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 4

    def test_articles_collection(self, workbook: Any) -> None:
        """
        Тестирование чтения сборника статей.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = ArticlesCollectionReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = ArticlesCollectionModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.article_title == "Наука как искусство"
        assert model.collection_title == "Сборник научных трудов"
        assert model.city == "СПб."
        assert model.publishing_house == "АСТ"
        assert model.year == 2020
        assert model.pages == "25-30"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 7

    def test_article_magazine(self, workbook: Any) -> None:
        """
        Тестирование чтения статьи из журнала.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = ArticleMagazineReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = ArticleMagazineModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.article_title == "Наука как искусство"
        assert model.magazine_title == "Сборник научных трудов"
        assert model.year == 2020
        assert model.number == 10
        assert model.pages == "25-30"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 6

    def test_law(self, workbook: Any) -> None:
        """
        Тестирование чтения закона т. д.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = LawReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = LawModel

        assert isinstance(model, model_type)
        assert model.type == "Конституция Российской Федерации"
        assert model.law_title == "Наука как искусство"
        assert model.passing_date == "01.01.2000"
        assert model.number == "1234-56"
        assert model.source == "Парламентская газета"
        assert model.source_year == 2020
        assert model.source_number == 5
        assert model.article_number == 15
        assert model.start_date == "11.09.2002"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 9

    def test_mla_book(self, workbook: Any) -> None:
        """
        Тестирование чтения иностранной криги.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = MLABookReader(workbook).read()

        assert len(models) == 2
        model = models[0]

        model_type = MLABookModel

        assert isinstance(model, model_type)
        assert model.author_last_name == "Smith"
        assert model.author_first_name == "Thomas"
        assert model.title == "The Citation Manual for Students: A Quick Guide"
        assert model.edition == "2nd"
        assert model.publisher == "Wiley"
        assert model.year == 2020

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 6

    def test_mla_internet_resource(self, workbook: Any) -> None:
        """
        Тестирование чтения иностранной криги.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = MLAInternetResourceReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = MLAInternetResourceModel

        assert isinstance(model, model_type)
        assert model.author_last_name == "Slat"
        assert model.author_first_name == "Boyan"
        assert model.title == "Whales Likely Impacted by Great Pacific Garbage Patch."
        assert model.website == "The Ocean Cleanup"
        assert model.publication_date == "10 Apr. 2019"
        assert model.url == "www.theoceancleanup.com/updates/whales-likely-impacted-by-great-pacific-garbage-patch"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 6

    def test_sources_reader(self) -> None:
        """
        Тестирование функции чтения всех моделей из источника.
        """

        models = SourcesReader(TEMPLATE_FILE_PATH).read()
        # проверка общего считанного количества моделей
        assert len(models) == 10

        # проверка наличия всех ожидаемых типов моделей среди типов считанных моделей
        model_types = {model.__class__.__name__ for model in models}
        assert model_types == {
            BookModel.__name__,
            InternetResourceModel.__name__,
            ArticlesCollectionModel.__name__,
            ArticleMagazineModel.__name__,
            LawModel.__name__,
            MLABookModel.__name__,
            MLAInternetResourceModel.__name__,
        }
