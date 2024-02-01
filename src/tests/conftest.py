"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, RegulatoryActModel, ArticleModel


@pytest.fixture
def book_model_fixture() -> BookModel:
    """
    Фикстура модели книги.

    :return: BookModel
    """

    return BookModel(
        authors="Иванов И.М., Петров С.Н.",
        title="Наука как искусство",
        edition="3-е",
        city="СПб.",
        publishing_house="Просвещение",
        year=2020,
        pages=999,
    )


@pytest.fixture
def internet_resource_model_fixture() -> InternetResourceModel:
    """
    Фикстура модели интернет-ресурса.

    :return: InternetResourceModel
    """

    return InternetResourceModel(
        article="Наука как искусство",
        website="Ведомости",
        link="https://www.vedomosti.ru",
        access_date="01.01.2021",
    )


@pytest.fixture
def articles_collection_model_fixture() -> ArticlesCollectionModel:
    """
    Фикстура модели сборника статей.

    :return: ArticlesCollectionModel
    """

    return ArticlesCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        collection_title="Сборник научных трудов",
        city="СПб.",
        publishing_house="АСТ",
        year=2020,
        pages="25-30",
    )


@pytest.fixture
def articles_model_fixture() -> ArticleModel:
    """
    Фикстура модели статьи из журнала.

    :return: ArticleModel
    """

    return ArticleModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        journal_name="Сборник научных трудов",
        No=2020,
        year=2020,
        pages="25-30",
    )

@pytest.fixture
def redulstory_act_model_fixture() -> RegulatoryActModel:
    """
    Фикстура модели нормативного актв.

    :return: ArticleModel
    """

    return RegulatoryActModel(
        act_type="Конституция Российской Федерации",
        full_name="Наука как искусство",
        acception_date="01.01.2000",
        act_No="1234-56",
        publishing_source="Парламентская газета",
        year=2020,
        source_No=5,
        article_No=15,
        amended_from="11.09.2002"
    )
