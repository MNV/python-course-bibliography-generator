"""
Тестирование функций оформления списка источников по Modern Language Association 9th edition.
"""

from src.formatters.base import BaseCitationFormatter
from src.formatters.models import MLABookModel, MLAInternetResourceModel
from src.formatters.styles.mla import MLABook, MLAInternetResource


class TestMLA:
    """
    Тестирование оформления списка источников согласно Modern Language Association 9th edition.
    """

    def test_mla_book(self, book_model_fixture: MLABookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги MLA
        :return:
        """

        model = MLABook(book_model_fixture)

        assert (
            model.formatted
            == "Smith, Thomas. The Citation Manual for Students: A Quick Guide. 2nd ed. Wiley, 2020."
        )

    def test_mla_internet_resource(
        self, internet_resource_model_fixture: MLAInternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = MLAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Slat, Boyan. “Whales Likely Impacted by Great Pacific Garbage Patch.” The Ocean Cleanup, "
               "10 Apr. 2019, www.theoceancleanup.com/updates/whales-likely-impacted-by-great-pacific-garbage-patch."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: MLABookModel,
        internet_resource_model_fixture: MLAInternetResourceModel,
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
        assert result[0] == models[0]
        assert result[1] == models[1]
