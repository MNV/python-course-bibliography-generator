"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""
from formatters.base import BaseCitationFormatter
from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    NormativeActModel,
    JournalArticleModel,
)
from formatters.styles.apa import (
    APABook,
    APAInternetResource,
    APACollectionArticle,
    APANormativeAct,
    APAJournalArticle,
)


class TestAPA:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
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
            == "Наука как искусство. (n.d.). Ведомости. Retrieved 01.01.2021, from https://www.vedomosti.ru"
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

    def test_journal_article(
        self, journal_article_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param JournalArticleModel journal_article_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = APAJournalArticle(journal_article_model_fixture)

        assert (
            model.formatted == "Анохин Н. В., Протас Н. Г., Шмаков Е. К. (2021). "
            "ИИС – шаг вперед, дающий рывок в будущее. Идеи и идеалы, 3, 266-280."
        )

    def test_normative_act(
        self, normative_act_model_fixture: NormativeActModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param NormativeActModel normative_act_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = APANormativeAct(normative_act_model_fixture)

        assert (
            model.formatted
            == "О персональных данных, Федеральный закон Российской Федерации No. 152-ФЗ, Stat. 5233 (27.07.2006)."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        normative_act_model_fixture: NormativeActModel,
        journal_article_model_fixture: JournalArticleModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param NormativeActModel normative_act_model_fixture: Фикстура модели нормативного акта
        :param JournalArticleModel journal_article_model_fixture: Фикстура модели статьи журнала
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APACollectionArticle(articles_collection_model_fixture),
            APANormativeAct(normative_act_model_fixture),
            APAJournalArticle(journal_article_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()
        # тестирование сортировки списка источников
        assert result[0] == models[4]
        assert result[1] == models[0]
        assert result[2] == models[2]
        assert result[3] == models[1]
        assert result[4] == models[3]
