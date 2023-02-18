"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    MagazineArticleModel,
    ThesisModel
)


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
def magazine_article_model_fixture() -> MagazineArticleModel:
    """
    Фикстура модели статьи из журнала

    :return: MagazineArticleModel
    """

    return MagazineArticleModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        magazine_title="Образование и наука",
        year=2020,
        volume=10,
        pages="25-30",
    )


@pytest.fixture
def thesis_model_fixture() -> ThesisModel:
    """
    Фикстура модели диссертации

    :return: ThesisModel
    """

    return ThesisModel(
        author="Иванов И.М.",
        title="Наука как искусство",
        degree="д-р. / канд.",
        field="экон.",
        code="01.01.01",
        city="СПб.",
        year=2020,
        pages=199,
    )
