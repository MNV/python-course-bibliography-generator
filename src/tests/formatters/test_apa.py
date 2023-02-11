"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, NewsPaperModel
from formatters.styles.apa import APABook, APAInternetResource, APANewsPaperResource


class TestAPA:
    """
    Тестирование оформления списка источников согласно APA
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
                == "Наука как искусство (01.01.2021) Ведомости https://www.vedomosti.ru"
        )

    def test_news_paper(
            self, newspaper_model_fixture: NewsPaperModel
    ) -> None:
        """
        Тестирование форматирования газеты.

        :param ArticlesCollectionModel newspaper_model_fixture: Фикстура модели газеты
        :return:
        """

        model = APANewsPaperResource(newspaper_model_fixture)

        assert (
                model.formatted
                == "Иванов И.М. (2020, 01.10). Наука как искусство. Южный Урал."
        )

    def test_citation_formatter(
            self,
            book_model_fixture: BookModel,
            internet_resource_model_fixture: InternetResourceModel,
            articles_collection_model_fixture: ArticlesCollectionModel,
            newspaper_model_fixture: NewsPaperModel
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel newspaper_model_fixture: Фикстура модели газеты
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APANewsPaperResource(newspaper_model_fixture)
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[2]
        assert result[1] == models[0]
        assert result[2] == models[1]
