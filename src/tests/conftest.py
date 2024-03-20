"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel,DissertationModel, RegulatoryActModel


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
        author_name="Иванов И.М.",
        title="Наука как искусство",
        author_title="д-р. / канд.",
        special_code="01.01.01",
        special_field="экон.",
        city="СПб.",
        year=2020,
        pages=199,
    )

@pytest.fixture
def regulatory_act_fixture() -> RegulatoryActModel:
    """
    Фикстура модели нормативного акта.
    :return: RegulatoryActModel
    """

    return RegulatoryActModel(
        type="Трудовой кодекс",
        name="Наука как искусство",
        agree_date="02.01.2022",
        act_num="8888-88",
        publishing_source="Сайт России",
        year=2022,
        source=5,
        article=15,
        amended_from="01.01.2021",
    )

