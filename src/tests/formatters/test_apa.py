"""
Тестирование функций оформления списка источников по APA 7th.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, DissertationModel, JournalArticleModel
from formatters.styles.apa import APABook, APAInternetResource, APACollectionArticle, APADissertation, APAJournalArticle


class TestGOST:
    """
    Тестирование оформления списка источников согласно APA 7th.
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
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. Просвещение."
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
            == "Наука как искусство (n.d.) Ведомости https://www.vedomosti.ru"
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. Сборник научных трудов, 25-30."
        )
    def test_journal_articles(
        self, journal_articles_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param JournalArticleModel journal_articles_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APAJournalArticle(journal_articles_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020). Наука как искусство. Образование и наука, 10, 25-30."
        )
    def test_dissertation(
        self, disseratation_model_fixture: DissertationModel
    ) -> None:
        """
        Тестирование форматирования диссертаций.

        :param DissertationModel disseratation_model_fixture: Фикстура модели диссертаций
        :return:
        """

        model = APADissertation(disseratation_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М. (2020). Наука как искусство [канд. диссиртация]"
        )
    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        disseratation_model_fixture: DissertationModel,
        journal_articles_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APACollectionArticle(articles_collection_model_fixture),
            APAJournalArticle(journal_articles_model_fixture),
            APADissertation(disseratation_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[3]
        assert result[1] == models[4]
        assert result[2] == models[2]
        assert result[3] == models[1]
        assert result[4] == models[0]
