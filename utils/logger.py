import logging


def get_logger(name: str) -> logging.Logger:
    """
    Логгер для приложения.

    :param name: __name__.
    :type name: str
    :return: Объект логгера.
    :rtype: logging.Logger
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.FileHandler("app.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
