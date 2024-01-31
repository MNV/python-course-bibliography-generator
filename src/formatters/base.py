"""
Базовые функции форматирования списка источников
"""
from typing import Dict

from pydantic import BaseModel

from formatters.styles.base import BaseCitationStyle
from logger import get_logger


logger = get_logger(__name__)


class BaseCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map: Dict[BaseModel, BaseCitationStyle]

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.

        :param models: Список объектов для итогового форматирования
        """
        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))  # type: ignore

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        logger.info("Общее форматирование ...")

        return sorted(self.formatted_items, key=lambda item: item.formatted)
