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
    Модель дисссертации:

    .. code-block::

        DissertationModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            degree="д-р. / канд.",
            branch="экон.",
            specialty_code="01.01.01",
            city="СПб.",
            year=2020,
            pages=199,
        )
    """
    author: str = Field(..., description="Фамилия и инициалы автора")
    title: str = Field(..., description="Название диссертации")
    degree: str = Field(..., description="Ученая степень (д-р. / канд.)")
    branch: str = Field(..., description="Отрасль наук (сокращённо)")
    specialty_code: str = Field(..., description="Код специальности")
    city: str = Field(..., description="Город издательства")
    year: int = Field(..., gt=0, description="Год защиты")
    pages: int = Field(..., gt=0, description="Количество страниц")

class AbstractModel(BaseModel):
    """
    Модель автореферата:

    .. code-block::

        AbstractModel(
            author="Иванов И.М.",
            title="Наука как искусство",
            degree="д-р. / канд.",
            branch="экон.",
            specialty_code="01.01.01",
            city="СПб.",
            year=2020,
            pages=199,
        )
    """

    author: str = Field(..., description="Фамилия и инициалы автора")
    title: str = Field(..., description="Название диссертации")
    degree: str = Field(..., description="Ученая степень (д-р. / канд.)")
    branch: str = Field(..., description="Отрасль наук (сокращённо)")
    specialty_code: str = Field(..., description="Код специальности")
    city: str = Field(..., description="Город издательства")
    year: int = Field(..., gt=0, description="Год издания")
    pages: int = Field(..., gt=0, description="Количество страниц")    