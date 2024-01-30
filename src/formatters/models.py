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


class RegulatoryActModel(BaseModel):
    """
    Модель нормативного акта:

    .. code-block::

        RegulatoryActModel(
            act_type="Конституция Российской Федерации",
            full_name="Наука как искусство",
            acception_date="01.01.2021",
            act_No="1234-56",
            publishing_source="Парламентская газета",
            year=2020,
            source_No=5,
            article_No=15,
            amended_from="01.01.2021",
        )
    """

    act_type: str
    full_name: str
    acception_date: str
    act_No: str
    publishing_source: str
    year: int = Field(..., gt=0)
    source_No: int = Field(..., gt=0)
    article_No:  int = Field(..., gt=0)
    amended_from : str


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
