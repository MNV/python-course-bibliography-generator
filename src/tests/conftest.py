"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    NewspaperCollectionModel,
    DissertationCollectionModel,
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
def newspaper_collection_model_fixture() -> NewspaperCollectionModel:
    """
    Фикстура модели статьи из газеты.

    :return: NewspaperCollectionModel
    """

    return NewspaperCollectionModel(
        authors="Иванов И.М., Петров С.Н.",
        article_title="Наука как искусство",
        newspaper_title="Южный Урал",
        year=1980,
        date="01.10",
        article_number=5,
    )


@pytest.fixture
def dissertation_collection_model_fixture() -> DissertationCollectionModel:
    """
    Фикстура модели диссертации.

    :return: DissertationCollectionModel
    """

    return DissertationCollectionModel(
        author="Иванов И.М.",
        dissertation_title="Наука как искусство",
        autor_grade="д-р. / канд.",
        science_branch="экон.",
        speciality_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=199,
    )
