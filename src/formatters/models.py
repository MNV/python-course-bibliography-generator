"""
Описание схем объектов (DTO).
"""

from typing import Optional

from pydantic import BaseModel, Field


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


class AbstractModel(BaseModel):
    """
    Модель автореферата:

    .. code-block::

        ArticlesCollectionModel(
            author="Иванов И.М.",
            abstract_title="Наука как искусство",
            author_status="д-р. / канд.",
            science_field="экон.",
            specialty_code="01.01.01",
            city="Спб.",
            year=2020,
            pages="199",
        )
    """

    author: str
    abstract_title: str
    author_status: str
    science_field: str
    specialty_code: str
    city: str
    year: int = Field(..., gt=0)
    pages: str


class RegulationModel(BaseModel):
    """
    Модель нормативного акта:

    .. code-block::

        ArticlesCollectionModel(
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
    """

    regulation_title: str
    source: str
    publishing_source: str
    regulation_id: str
    acceptance_date: str
    publishing_year: int = Field(..., gt=0)
    publishing_source_id: str
    publishing_article_id: str
    modification_date: str


class NewsPaperModel(BaseModel):
    """
    Модель газеты:

    .. code-block::

        NewsPaperModel(
            article_title="Наука как искусство",
            authors="Иванов И.М., Петров С.Н.",
            news_title="Южный Урал",
            publishing_year="1980",
            publishing_date="01.10",
            publishing_number="5"
        )
    """

    article_title: str
    authors: str
    news_title: str
    publishing_year: int = Field(..., gt=0)
    publishing_date: str
    publishing_number: int = Field(..., gt=0)
