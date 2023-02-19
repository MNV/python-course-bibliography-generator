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


class ArticleMagazineModel(BaseModel):
    """
    Модель статьи из журнала:

    .. code-block::

        ArticleMagazineModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            magazine_title="Сборник научных трудов,
            year=2020,
            number=10,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    magazine_title: str
    year: int = Field(..., gt=0)
    number: int = Field(..., gt=0)
    pages: str


class LawModel(BaseModel):
    """
    Модель закона, нормативного актa и т.п.:

    .. code-block::

        LawModel(
            type="Конституция Российской Федерации",
            law_title="Наука как искусство",
            passing_date="01.01.2000",
            number="1234-56",
            source="Парламентская газета",
            source_year=2020,
            source_number=5,
            article_number=15,
            start_date="11.09.2002",
        )
    """

    type: str
    law_title: str
    passing_date: str
    number: str
    source: str
    source_year: int = Field(..., gt=0)
    source_number: int = Field(..., gt=0)
    article_number: int = Field(..., gt=0)
    start_date: str


class MLABookModel(BaseModel):
    """
    Модель книги MLA:

    .. code-block::

        MLABookModel(
            author_last_name="Smith",
            author_first_name="Thomas",
            title="",
            edition="",
            publisher="",
            year=2020,
        )
    """

    author_last_name: str
    author_first_name: str
    title: str
    edition: Optional[str]
    publisher: str
    year: int = Field(..., gt=0)


class MLAInternetResourceModel(BaseModel):
    """
    Модель интернет ресурса MLA:

    .. code-block::

        MLAInternetResourceModel(
            author_last_name="Smith",
            author_first_name="Thomas",
            title: "Whales Likely Impacted by Great Pacific Garbage Patch."
            website: "The Ocean Cleanup"
            publication_date="10 Apr. 2019",
            url="www.theoceancleanup.com/updates/whales-likely-impacted-by-great-pacific-garbage-patch",
        )
    """

    author_last_name: str
    author_first_name: str
    title: str
    website: str
    publication_date: str
    url: str
