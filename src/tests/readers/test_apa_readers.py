"""
Тестирование функций чтения данных из источника.
"""
from typing import Any

import pytest

from formatters.models import (
    InternetResourceModel,
    MagazineArticleModel,
)
from readers.apa_reader import (
    APAReader,
    InternetResourceReader,
    MagazineArticleReader,
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

        return APAReader(TEMPLATE_FILE_PATH).workbook

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

    def test_magazine_article(self, workbook: Any) -> None:
        """
        Тестирование чтения статьи из журнала.

        :param workbook: Объект тестовой рабочей книги.
        """

        models = MagazineArticleReader(workbook).read()

        assert len(models) == 1
        model = models[0]

        model_type = MagazineArticleModel

        assert isinstance(model, model_type)
        assert model.authors == "Иванов И.М., Петров С.Н."
        assert model.article_title == "Наука как искусство"
        assert model.magazine_title == "Образование и наука"
        assert model.year == 2020
        assert model.volume == "10"
        assert model.pages == "25-30"

        # проверка общего количества атрибутов
        assert len(model_type.schema().get("properties", {}).keys()) == 6

    def test_sources_reader(self) -> None:
        """
        Тестирование функции чтения всех моделей из источника.
        """

        models = APAReader(TEMPLATE_FILE_PATH).read()
        # проверка общего считанного количества моделей
        assert len(models) == 4

        # проверка наличия всех ожидаемых типов моделей среди типов считанных моделей
        model_types = {model.__class__.__name__ for model in models}
        assert model_types == {
            InternetResourceModel.__name__,
            MagazineArticleModel.__name__,
        }
