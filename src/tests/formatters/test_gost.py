"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    AbstractModel,
    RegulationModel,
)
from formatters.styles.gost import (
    GOSTBook,
    GOSTInternetResource,
    GOSTCollectionArticle,
    GOSTAbtract,
    GOSTRegulation,
)


class TestGOST:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = GOSTBook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство. – 3-е изд. – СПб.: Просвещение, 2020. – 999 с."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = GOSTInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство // Ведомости URL: https://www.vedomosti.ru (дата обращения: 01.01.2021)."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = GOSTCollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Сборник научных трудов. – СПб.: АСТ, 2020. – С. 25-30."
        )

    def test_abstract(self, abstract_model_fixture: AbstractModel) -> None:
        """
        Тестирование форматирования автореферата.

        :param AbstractModel abstract_model_fixture: Фикстура модели автореферата
        :return:
        """

        model = GOSTAbtract(abstract_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. Наука как искусство: автореф. дис. ... д-р. / канд. экон. наук: 01.01.01. Спб., "
            "2020. 199 с."
        )

    def test_regulation(self, regulation_model_fixture: RegulationModel) -> None:
        """
        Тестирование форматирования нормативного акта.

        :param RegulationModel regulation_model_fixture: Фикстура модели нормативного акта
        :return:
        """

        model = GOSTRegulation(regulation_model_fixture)

        assert (
            model.formatted
            == 'Конституция Российской Федерации "Наука как искусство" от 1/1/2000 № 1234-56 // Парламентская '
            "газета. 2020 г. № 5. Ст. 15 с изм. и допол. в ред. от 9/11/2002"
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        abstract_model_fixture: AbstractModel,
        regulation_model_fixture: RegulationModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param AbstractModel abstract_model_fixture: Фикстура модели автореферата
        :param RegulationModel regulation_model_fixture: Фикстура модели нормативного акта
        :return:
        """

        models = [
            GOSTBook(book_model_fixture),
            GOSTInternetResource(internet_resource_model_fixture),
            GOSTCollectionArticle(articles_collection_model_fixture),
            GOSTAbtract(abstract_model_fixture),
            GOSTRegulation(regulation_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[3]
        assert result[1] == models[2]
        assert result[2] == models[0]
        assert result[3] == models[4]
        assert result[4] == models[1]
