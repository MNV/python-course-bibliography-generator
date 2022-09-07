"""
Базовые методы для форматирования списка источников.
"""

from abc import ABC, abstractmethod
from string import Template

from pydantic import BaseModel


class BaseCitationStyle(ABC):
    """
    Абстрактный базовый класс стиля цитирования.
    """

    def __init__(self, data: BaseModel) -> None:
        self.data = data
        self.formatted = self.substitute()

    @property
    @abstractmethod
    def template(self) -> Template:
        """
        Получение шаблона для форматирования строки.

        :return:
        """

    @abstractmethod
    def substitute(self) -> str:
        """
        Заполнение шаблона для форматирования строки.

        :return:
        """

    def __str__(self) -> str:
        return self.formatted

    def __repr__(self) -> str:
        return self.formatted
