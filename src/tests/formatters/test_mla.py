"""
Тестирование функций оформления списка источников по MLA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, RegulatoryActModel, ArticleModel
from formatters.styles.mla import MLABook, MLAInternetResource, MLACollectionArticle, MLARegulatoryAct, MLAArticle


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
            == "Иванов И.М., Петров С.Н. Наука как искусство. 3rd ed., СПб.: Просвещение, 2020."
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
            == '"Наука как искусство." Ведомости, https://www.vedomosti.ru. Accessed 01.01.2021.'
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = MLACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == 'Иванов И.М., Петров С.Н. "Наука как искусство." Сборник научных трудов, АСТ, 2020, pp. 25-30.'
        )

    def test_articles(
        self, articles_model_fixture: ArticleModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesModel articles_model_fixture: Фикстура модели статей
        :return:
        """

        model = MLAArticle(articles_model_fixture)

        assert (
            model.formatted
            == 'Иванов И.М. and  Петров С.Н. "Наука как искусство." Образование и наука, no. 10, 2020, pp. 25-30.'
        )

    def test_regulatory_act(
        self, regulatory_act_model_fixture: RegulatoryActModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param RegulatoryActModel regulatory_act_model_fixture: Фикстура модели сборника нормативных актов
        :return:
        """

        model = MLARegulatoryAct(regulatory_act_model_fixture)

        assert (
            model.formatted
            == 'Наука как искусство. Pub L. 1234-56. 01.01.2000. Парламентская газета.'
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        articles_model_fixture: ArticleModel,
        regulatory_act_model_fixture: RegulatoryActModel
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        models = [
            MLABook(book_model_fixture),
            MLAInternetResource(internet_resource_model_fixture),
            MLACollectionArticle(articles_collection_model_fixture),
            MLAArticle(articles_model_fixture),
            MLARegulatoryAct(regulatory_act_model_fixture)
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[3]
        assert result[2] == models[2]
        assert result[3] == models[0]
        assert result[4] == models[4]
