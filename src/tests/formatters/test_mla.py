"""
Тестирование функций оформления списка источников по MLA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel
from formatters.styles.mla import MLABook, MLAInternetResource


class TestMLA:
    """
    Тестирование оформления списка источников согласно MLA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = MLABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н.. Наука как искусство. Просвещение, 2020."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = MLAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == '"Наука как искусство". Ведомости, 01.01.2021. https://www.vedomosti.ru.'
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        models = [
            MLABook(book_model_fixture),
            MLAInternetResource(internet_resource_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[0]
