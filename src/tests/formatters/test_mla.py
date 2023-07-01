"""
Тестирование функций оформления списка источников по MLA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, DissertationModel, ArticleFromTheJournalModel
from formatters.styles.MLA import MLABook, MLAInternetResource, MLACollectionArticle, MLADissertation, MLAArticleFromTheJournal

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
            == "Иванов И.М., Петров С.Н.. Наука как искусство. 3-е изд., СПб.: Просвещение, 2020"
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
            == "Наука как искусство. Ведомости, 01.01.2021, https://www.vedomosti.ru"
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
            == "Иванов И.М., Петров С.Н.. Наука как искусство. Сборник научных трудов. СПб., АСТ, 2020, с.25-30."
        )

    def test_dissertation(
        self, dissertation_model_fixture: DissertationModel
    ) -> None:
        """
        Тестирование форматирования диссертации.

        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :return:
        """

        model = MLADissertation(dissertation_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М.. Наука как искусство.2020. СПб.. д-р. / канд. экон. наук."
        )

    def test_article_from_the_journal(
        self, article_from_the_journal_model_fixture: ArticleFromTheJournalModel
    ) -> None:
        """
        Тестирование форматирования статьи в журнале.

        :param ArticleFromTheJournalModel article_from_the_journal_model_fixture: Фикстура модели статьи журнала
        :return:
        """

        model = MLAArticleFromTheJournal(article_from_the_journal_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н.. Наука как искусство. Образование и наука,(10),2020,с.25-30."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        dissertation_model_fixture: DissertationModel,
        article_from_the_journal_model_fixture: ArticleFromTheJournalModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :param ArticleFromTheJournalModel article_from_the_journal_model_fixture: Фикстура модели статьи журнала
        :return:
        """

        models = [
            MLABook(book_model_fixture),
            MLAInternetResource(internet_resource_model_fixture),
            MLACollectionArticle(articles_collection_model_fixture),
            MLADissertation(dissertation_model_fixture),
            MLAArticleFromTheJournal(article_from_the_journal_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()
        
        # тестирование сортировки списка источников 
        assert result[0] == models[0]
        assert result[1] == models[4]
        assert result[2] == models[2]
        assert result[3] == models[3]
        assert result[4] == models[1]