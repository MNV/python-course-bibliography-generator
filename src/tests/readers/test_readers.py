"""
Тестирование функций чтения данных из источника.
"""
from typing import Any

import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, DissertationModel, RegulatoryActModel
from readers.reader import (
    BookReader,
    SourcesReader,
    InternetResourceReader,
    ArticlesCollectionReader, DissertationReader, RegulatoryActReader
)
from settings import TEMPLATE_FILE_PATH


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

    def test_dissertation(self, workbook: Any) -> None:
        """
        Тестирование чтения диссертации.
        :param workbook: Объект тестовой рабочей книги.
        """

        models = DissertationReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = DissertationModel

        assert isinstance(model, model_type)
        assert model.author_name == "Иванов И.М."
        assert model.title == "Наука как искусство"
        assert model.author_title == "д-р. / канд."
        assert model.special_field == "01.01.01"
        assert model.special_code == "экон."
        assert model.city == "СПб."
        assert model.year == 2020
        assert model.pages == 199

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 8

    def test_regulatory_act(self, workbook: Any) -> None:
        """
        Тестирование чтения нормативных актов.
        :param workbook: Объект тестовой рабочей книги.
        """

        models = RegulatoryActReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = RegulatoryActModel

        assert isinstance(model, model_type)
        assert model.type == "Конституция Российской Федерации"
        assert model.name == "Наука как искусство"
        assert model.agree_date == "2000-01-01 00:00:00"
        assert model.act_num == "1234-56"
        assert model.publishing_source == "Парламентская газета"
        assert model.year == 2020
        assert model.source == 5
        assert model.article == 15
        assert model.amended_from == "2002-09-11 00:00:00"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 9

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
            DissertationModel.__name__,
            RegulatoryActModel.__name__
        }
