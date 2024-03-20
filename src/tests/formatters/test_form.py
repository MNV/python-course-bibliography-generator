"""
Тестирование функций оформления списка источников по APA
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel
from formatters.styles.apa import Book_APA, InternetResource_APA


class Test_APA:
    """
    Тестирование оформления списка источников по стандарту APA
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книг по стандарту APA.
        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = Book_APA(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство (3-е изд.). Просвещение."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса по стандарту APA.
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = InternetResource_APA(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство. (n.d.). Ведомости. Retrieved 01.01.2021, from https://www.vedomosti.ru"
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
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей

        :return:
        """

        models = [
            Book_APA(book_model_fixture),
            InternetResource_APA(internet_resource_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[0]
        assert result[1] == models[1]