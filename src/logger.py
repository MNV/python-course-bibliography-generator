"""
Функции для логирования.
"""
import logging

from src.settings import LOGGING_FORMAT, LOGGING_LEVEL, LOGGING_PATH


def get_logger(
    module_name: str,
    logging_level: str = LOGGING_LEVEL,
    logging_format: str = LOGGING_FORMAT,
) -> logging.Logger:
    """
    Настройка логгера.

    :param module_name: Наименование модуля
    :param logging_level: Уровень логирования
    :param logging_format: Формат логов
    :return:
    """

    # запись логов в файлы
    logger = logging.getLogger(module_name)
    logger.setLevel(logging_level)
    file_handler = logging.FileHandler(f"{LOGGING_PATH}/{module_name}.log")
    file_handler.setFormatter(logging.Formatter(logging_format))
    logger.addHandler(file_handler)

    # вывод логов в консоль
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(logging_format))
    logger.addHandler(stream_handler)

    return logger
