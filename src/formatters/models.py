"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


class JournalArticleModel(BaseModel):
    """
    Модель статьи из журнала:

    .. code-block::

        JournalArticleModel(
            authors="Анохин Н. В., Протас Н. Г., Шмаков Е. К.",
            article_title="ИИС – шаг вперед, дающий рывок в будущее",
            journal_name="Идеи и идеалы",
            publication_year=2021,
            journal_number=3,
            pages="266-280",
        )
    """

    authors: str
    article_title: str
    journal_name: str
    publication_year: int = Field(..., gt=0)
    journal_number: int
    pages: str


class NormativeActModel(BaseModel):
    """
    Модель нормативного акта, закона:

    .. code-block::

        NormativeActModel(
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
    """

    type: str
    title: str
    adoption_date: str
    act_numer: str
    source: str
    publication_year: int = Field(..., gt=0)
    source_number: int
    article_number: int
    revision: str


class BookModel(BaseModel):
    """
    Модель книги:

    .. code-block::

        BookModel(
            authors="Иванов И.М., Петров С.Н.",
            title="Наука как искусство",
            edition="3-е",
            city="СПб.",
            publishing_house="Просвещение",
            year=2020,
            pages=999,
        )
    """

    authors: str
    title: str
    edition: Optional[str]
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


class InternetResourceModel(BaseModel):
    """
    Модель интернет ресурса:

    .. code-block::

        InternetResourceModel(
            article="Наука как искусство",
            website="Ведомости",
            link="https://www.vedomosti.ru/",
            access_date="01.01.2021",
        )
    """

    article: str
    website: str
    link: str
    access_date: str


class ArticlesCollectionModel(BaseModel):

    """
    Модель сборника статей:

    .. code-block::

        ArticlesCollectionModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            collection_title="Сборник научных трудов",
            city="СПб.",
            publishing_house="АСТ",
            year=2020,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    collection_title: str
    city: str
    publishing_house: str
    year: int = Field(..., gt=0)
    pages: str
