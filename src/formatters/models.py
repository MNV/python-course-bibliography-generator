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

class DissertationModel(BaseModel):
    """
    Модель диссертации:
    .. code-block::
        DissertationModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            academic_degree="канд.",
            science="экон.",
            specialty_code="01.01.01",
            publication_city="СПб.",
            publication_year=2020,
            page_count=199,
        )
    """

    author: str
    title: str
    academic_degree: str
    science: str
    specialty_code: str
    publication_city: str
    publication_year: int = Field(..., gt=0)
    page_count: int = Field(..., gt=0)


class ArticleNewspaperModel(BaseModel):
    """
    Модель статьи из газеты:
    .. code-block::
        NewspaperArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            newspaper_name="Южный Урал",
            publication_year=1980,
            publication_date="01.10",
            аrticle_number=5
        )
    """

    authors: str
    article_title: str
    newspaper_name: str
    publication_year: int = Field(..., gt=0)
    publication_date: str
    аrticle_number: int = Field(..., gt=0)
