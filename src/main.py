"""
Запуск приложения.
"""
from enum import Enum, unique

import click

from src.formatters.styles.mla import MLACitationFormatter
from src.formatters.styles.gost import GOSTCitationFormatter

from logger import get_logger
from readers.reader import SourcesReader, MLASourcesReader
from renderer import Renderer
from settings import INPUT_FILE_PATH, OUTPUT_FILE_PATH, OUTPUT_MLA_FILE_PATH

logger = get_logger(__name__)


@unique
class CitationEnum(Enum):
    """
    Поддерживаемые типы цитирования.
    """

    GOST = "gost"  # ГОСТ Р 7.0.5-2008
    MLA = "mla"  # Modern Language Association
    APA = "apa"  # American Psychological Association


@click.command()
@click.option(
    "--citation",
    "-c",
    "citation",
    type=click.Choice([item.name for item in CitationEnum], case_sensitive=False),
    default=CitationEnum.GOST.name,
    show_default=True,
    help="Стиль цитирования",
)
@click.option(
    "--path_input",
    "-pi",
    "path_input",
    type=str,
    default=INPUT_FILE_PATH,
    show_default=True,
    help="Путь к входному файлу",
)
@click.option(
    "--path_output",
    "-po",
    "path_output",
    type=str,
    default=OUTPUT_FILE_PATH,
    show_default=True,
    help="Путь к выходному файлу",
)
def process_input_gost(
    citation: str = CitationEnum.GOST.name,
    path_input: str = INPUT_FILE_PATH,
    path_output: str = OUTPUT_FILE_PATH,
) -> None:
    """
    Генерация файла Word с оформленным библиографическим списком.

    :param str citation: Стиль цитирования
    :param str path_input: Путь к входному файлу
    :param str path_output: Путь к выходному файлу
    """

    logger.info(
        """Обработка команды с параметрами:
        - Стиль цитирования: %s.
        - Путь к входному файлу: %s.
        - Путь к выходному файлу: %s.""",
        citation,
        path_input,
        path_output,
    )

    models = SourcesReader(path_input).read()
    formatted_models = tuple(
        str(item) for item in GOSTCitationFormatter(models).format()
    )

    logger.info("Генерация выходного файла ...")
    Renderer(formatted_models).render(path_output)

    logger.info("Команда успешно завершена.")


def process_input_mla(
    citation: str = CitationEnum.MLA.name,
    path_input: str = INPUT_FILE_PATH,
    path_output: str = OUTPUT_MLA_FILE_PATH,
) -> None:
    """
    Генерация файла Word с оформленным библиографическим списком.

    :param str citation: Стиль цитирования
    :param str path_input: Путь к входному файлу
    :param str path_output: Путь к выходному файлу
    """

    logger.info(
        """Обработка команды с параметрами:
        - Стиль цитирования: %s.
        - Путь к входному файлу: %s.
        - Путь к выходному файлу: %s.""",
        citation,
        path_input,
        path_output,
    )

    models = MLASourcesReader(path_input).read()
    formatted_models = tuple(
        str(item) for item in MLACitationFormatter(models).format()
    )

    logger.info("Генерация выходного файла ...")
    Renderer(formatted_models).render(path_output)

    logger.info("Команда успешно завершена.")


if __name__ == "__main__":
    try:
        # запуск обработки входного файла
        process_input_mla()
        process_input_gost()
    except Exception as ex:
        logger.error("При обработке команды возникла ошибка: %s", ex)
        raise
