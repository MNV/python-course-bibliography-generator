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


class RegulatoryActModel(BaseModel):
    """
    Модель нормативного акта:
    .. code-block::
        RegulatoryActModel(
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
    """

    type: str
    name: str
    agree_date: str
    act_num: str
    publishing_source: str
    year: int = Field(..., gt=0)
    source: int = Field(..., gt=0)
    article: int = Field(..., gt=0)
    amended_from: str


class DissertationModel(BaseModel):
    """
    Модель диссертации:
    .. code-block::
        DissertationModel(
            author_name="Петров С.Н.",
            title="Наука как искусство",
            author_title="канд.",
            special_field="ЭВМ.",
            special_code="09.01.02",
            city="СПб.",
            year=2022,
            pages=199,
        )
    """

    author_name: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    author_title: str = Field(..., min_length=1)
    special_field: str = Field(..., min_length=1)
    special_code: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)
    pages: int = Field(..., gt=0)


