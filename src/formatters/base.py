"""
Базовые функции форматирования списка источников
"""

from src.formatters.styles.base import BaseCitationStyle
from src.logger import get_logger


logger = get_logger(__name__)


class BaseCitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    def __init__(self, formatted_items: list[BaseCitationStyle]) -> None:
        """
        Конструктор.
        :param formatted_items: Список объектов для итогового форматирования
        """

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.

        :return:
        """

        logger.info("Общее форматирование ...")

        return sorted(self.formatted_items, key=lambda item: item.formatted)
