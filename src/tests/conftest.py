"""
Фикстуры для моделей объектов (типов источников).
"""
import pytest

from formatters.models import (
    BookModel,
    InternetResourceModel,
    ArticlesCollectionModel,
    NormativeActModel,
    JournalArticleModel,
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
def normative_act_model_fixture() -> NormativeActModel:
    """
    Фикстура модели нормативного акта.

    :return: ArticlesCollectionModel
    """

    return NormativeActModel(
        type="Федеральный закон Российской Федерации",
        title="О персональных данных",
        adoption_date="27.07.2006",
        act_numer="152-ФЗ",
        source="Собрание законодательства Российской Федерации",
        publication_year=2006,
        source_number=29,
        article_number=5233,
        revision="06.02.2023",
    )


@pytest.fixture
def journal_article_model_fixture() -> JournalArticleModel:
    """
    Фикстура модели статьи из журнала.

    :return: ArticlesCollectionModel
    """

    return JournalArticleModel(
        authors="Анохин Н. В., Протас Н. Г., Шмаков Е. К.",
        article_title="ИИС – шаг вперед, дающий рывок в будущее",
        journal_name="Идеи и идеалы",
        publication_year=2021,
        journal_number=3,
        pages="266-280",
    )
