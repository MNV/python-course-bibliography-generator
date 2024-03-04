"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    DissertationModel,
    AbstractModel,
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
def dissertation_fixture() -> DissertationModel:
    """
    Фикстура модели диссертации.
    :return: DissertationModel
    """

    return DissertationModel(
        author="Иванов И.М.",
        title="Наука как искусство",
        degree="д-р. / канд.",
        branch="экон.",
        speciality_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=199,
    )


@pytest.fixture
def abstract_fixture() -> AbstractModel:
    """
    Фикстура модели автореферата.
    :return: DissertationModel
    """

    return AbstractModel(
        author="Иванов И.М.",
        title="Наука как искусство",
        degree="д-р. / канд.",
        branch="экон.",
        speciality_code="01.01.01",
        city="СПб.",
        year=2020,
        pages=199,
    )
