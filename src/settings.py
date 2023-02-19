"""
Настройки проекта.
"""

import os

# путь к файлу шаблона для создания входного файла
TEMPLATE_FILE_PATH: str = os.getenv("TEMPLATE_FILE_PATH", "../media/template.xlsx")

# путь к входному файлу
INPUT_FILE_PATH: str = os.getenv("INPUT_FILE_PATH", "../media/input.xlsx")
# путь к выходным файлам
OUTPUT_FILE_PATH: str = os.getenv("OUTPUT_FILE_PATH", "../media/output_gost.docx")
OUTPUT_MLA_FILE_PATH: str = os.getenv("OUTPUT_MLA_FILE_PATH", "../media/output_mla.docx")

# путь к директории для логирования
LOGGING_PATH: str = os.getenv("LOGGING_PATH", "../logs")
# формат для записей логов
LOGGING_FORMAT: str = os.getenv(
    "LOGGING_FORMAT", "%(name)s %(asctime)s %(levelname)s %(message)s"
)
# уровень логирования
LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "INFO")
