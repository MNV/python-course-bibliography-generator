"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from src.formatters.base import BaseCitationFormatter
from src.formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, ArticleMagazineModel, \
    LawModel
from src.formatters.styles.gost import GOSTBook, GOSTInternetResource, GOSTCollectionArticle, GOSTMagazineArticle, \
    GOSTLaw


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

    def test_article_magazine(
        self, article_magazine_model_fixture: ArticleMagazineModel
    ) -> None:
        """
        Тестирование форматирования статьи из журнала.

        :param ArticleMagazineModel article_magazine_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = GOSTMagazineArticle(article_magazine_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. Наука как искусство // Образование и наука. – 2020. – №10. – С. 25-30."
        )

    def test_law(
        self, law_model_fixture: LawModel
    ) -> None:
        """
        Тестирование форматирования закона и т. д.

        :param LawModel law_model_fixture: Фикстура модели закона и т. д.
        :return:
        """

        model = GOSTLaw(law_model_fixture)

        assert (
            model.formatted
            == "Конституция Российской Федерации \"Наука как искусство\" от 01.01.2000 № 1234-56 // Парламентская газета. - 2020 г. - № 5. - Ст. 15 с изм. и допол. в ред. от 11.09.2002."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        models = [
            GOSTBook(book_model_fixture),
            GOSTInternetResource(internet_resource_model_fixture),
            GOSTCollectionArticle(articles_collection_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[2]
        assert result[1] == models[0]
        assert result[2] == models[1]
