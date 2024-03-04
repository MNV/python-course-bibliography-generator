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


class JournalArticleModel(BaseModel):

    """
    Модель статьи из журнала:

    .. code-block::

        JournalArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            journal_title="Образование и наука",
            year=2020,
            journal_issue=10,
            pages="25-30",
        )
    """

    authors: str
    article_title: str
    journal_title: str
    year: int = Field(..., gt=0)
    journal_issue: int = Field(..., gt=0)
    pages: str


class NewspaperArticleModel(BaseModel):

    """
    Модель статьи из газеты:

    .. code-block::

        NewspaperArticleModel(
            authors="Иванов И.М., Петров С.Н.",
            article_title="Наука как искусство",
            newspaper_title="Южный Урал",
            year=1980,
            date="01.10",
            article_number=5,
        )
    """

    authors: str
    article_title: str
    newspaper_title: str
    year: int = Field(..., gt=0)
    date: str
    article_number: int = Field(..., gt=0)
