"""
Тестирование функций оформления списка источников по ГОСТ Р 7.0.5-2008.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import (
    InternetResourceModel,
    MagazineArticleModel,
)
from formatters.styles.apa import (
    APAInternetResource,
    APAMagazineArticle,
)


class TestAPA:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

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
                == "Наука как искусство // Ведомости URL: https://www.vedomosti.ru (дата обращения: 01.01.2021)."
        )

    def test_magazine_article(
            self, magazine_article_model_fixture: MagazineArticleModel
    ) -> None:
        """
        Тестирование форматирования статьи из журнала.

        :param MagazineArticleModel magazine_article_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        model = APAMagazineArticle(magazine_article_model_fixture)

        assert (
                model.formatted
                == "Иванов И.М., Петров С.Н. Наука как искусство // Образование и наука. 2020. Т. 10. С. 25-30."
        )

    def test_citation_formatter(
            self,
            internet_resource_model_fixture: InternetResourceModel,
            magazine_article_model_fixture: MagazineArticleModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param MagazineArticleModel magazine_article_model_fixture: Фикстура модели статьи из журнала
        :return:
        """

        models = [
            APAInternetResource(internet_resource_model_fixture),
            APAMagazineArticle(magazine_article_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[0]
