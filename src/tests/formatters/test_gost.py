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
from formatters.styles.gost import (
    GOSTBook,
    GOSTInternetResource,
    GOSTCollectionArticle,
    GOSTNormativeAct,
    GOSTJournalArticle,
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

    def test_journal_article(
        self, journal_article_model_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param JournalArticleModel journal_article_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = GOSTJournalArticle(journal_article_model_fixture)

        assert (
            model.formatted
            == "Анохин Н. В., Протас Н. Г., Шмаков Е. К. ИИС – шаг вперед, дающий рывок в "
            "будущее // Идеи и идеалы. 2021. № 3, С. 266-280."
        )

    def test_normative_act(
        self, normative_act_model_fixture: NormativeActModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param NormativeActModel normative_act_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = GOSTNormativeAct(normative_act_model_fixture)

        assert (
            model.formatted
            == "О персональных данных : Федеральный закон Российской Федерации от 27.07.2006 "
            "№ 152-ФЗ // Собрание законодательства Российской Федерации. 2006. №29. Ст. 5233. в ред. от 06.02.2023."
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
            GOSTBook(book_model_fixture),
            GOSTInternetResource(internet_resource_model_fixture),
            GOSTCollectionArticle(articles_collection_model_fixture),
            GOSTNormativeAct(normative_act_model_fixture),
            GOSTJournalArticle(journal_article_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()
        # тестирование сортировки списка источников
        assert result[0] == models[4]
        assert result[1] == models[2]
        assert result[2] == models[0]
        assert result[3] == models[1]
        assert result[4] == models[3]
