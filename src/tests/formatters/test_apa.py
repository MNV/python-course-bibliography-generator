"""
Тестирование функций оформления списка источников по American Psychological Association.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel
from formatters.styles.apa import APABook, APAInternetResource


class TestGOST:
    """
    Тестирование оформления списка источников согласно American Psychological Association.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. & Петров С.Н. (2020). /i/Наука как искусство./i/ Просвещение."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости. (01.01.2021). /i/Наука как искусство./i/ Ведомости. https://www.vedomosti.ru"
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
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[0]
