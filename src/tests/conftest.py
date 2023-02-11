"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, AbstractModel, \
    RegulationModel, NewsPaperModel


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
def abstract_model_fixture() -> AbstractModel:
    """
    Фикстура модели автореферата.

    :return: AbstractModel
    """

    return AbstractModel(
        author="Иванов И.М.",
        abstract_title="Наука как искусство",
        author_status="д-р. / канд.",
        science_field="экон.",
        specialty_code="01.01.01",
        city="Спб.",
        year=2020,
        pages="199"
    )


@pytest.fixture
def regulation_model_fixture() -> RegulationModel:
    """
    Фикстура модели нормативного акта.

    :return: RegulationModel
    """

    return RegulationModel(
        regulation_title="Наука как искусство",
        source="Конституция Российской Федерации",
        publishing_source="Парламентская газета",
        regulation_id="1234-56",
        acceptance_date="1/1/2000",
        publishing_year="2020",
        publishing_source_id="5",
        publishing_article_id="15",
        modification_date="9/11/2002"
    )


@pytest.fixture
def newspaper_model_fixture() -> NewsPaperModel:
    """
    Фикстура модели газеты.

    :return: NewsPaperModel
    """

    return NewsPaperModel(
        article_title="Наука как искусство",
        authors="Иванов И.М.",
        news_title="Южный Урал",
        publishing_year="2020",
        publishing_date="01.10",
        publishing_number="5"
    )
