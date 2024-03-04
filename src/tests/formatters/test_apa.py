"""
Тестирование функций оформления списка источников по APA.
"""
from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    AbstractModel,
)
from formatters.styles.apa import (
    APABookFormatter,
    APAInternetResourceFormatter,
    APACollectionArticleFormatter,
    APADissertationFormatter,
    APAAbstractFormatter,
)


class TestAPA:
    """
    Тестирование оформления списка источников согласно стилю APA.
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги в стиле APA.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABookFormatter(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И. & Петров С. (2020). Наука как искусство. (3-е изд.). СПб.: Просвещение."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса в стиле APA.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResourceFormatter(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Наука как искусство (б. д.). Ведомости URL: https://www.vedomosti.ru (дата обращения: 01.01.2021)."
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей в стиле APA.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APACollectionArticleFormatter(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И. & Петров С. (2020). Наука как искусство. Сборник научных трудов (pp. 25-30). СПб.: АСТ."
        )

    def test_dissertation(self, dissertation_fixture: DissertationModel) -> None:
        """
        Тестирование форматирования диссертации в стиле APA.
        :param DissertationModel dissertation_fixture: Фикстура модели диссертации
        :return:
        """

        model = APADissertationFormatter(dissertation_fixture)

        assert (
            model.formatted
            == "Иванов И.М.. (2020). Наука как искусство (д-р. / канд.) [Диссертация]. экон., 01.01.01. СПб."
        )

    def test_abstract(self, abstract_fixture: AbstractModel) -> None:
        """
        Тестирование форматирования автореферата в стиле APA.
        :param AbstractModel abstract_fixture: Фикстура модели автореферата
        :return:
        """

        model = APAAbstractFormatter(abstract_fixture)

        assert (
            model.formatted
            == "Иванов И.М.. (2020). Наука как искусство (д-р. / канд.) [Автореферат]. экон., 01.01.01. СПб."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        dissertation_fixture: DissertationModel,
        abstract_fixture: AbstractModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param DissertationModel dissertation_fixture: Фикстура модели диссертации
        :param AbstractModel abstract_fixture: Фикстура модели автореферата
        :return:
        """

        models = [
            APABookFormatter(book_model_fixture),
            APAInternetResourceFormatter(internet_resource_model_fixture),
            APACollectionArticleFormatter(articles_collection_model_fixture),
            APADissertationFormatter(dissertation_fixture),
            APAAbstractFormatter(abstract_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # Тестирование сортировки списка источников
        assert result[0] == models[0]
        assert result[1] == models[2]
        assert result[2] == models[4]
        assert result[3] == models[3]
        assert result[4] == models[1]
