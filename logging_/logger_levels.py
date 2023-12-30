"""
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
"""
import logging

# задать дефолтный уровень логирования для новых логгеров
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
# установить уровень отличный от дефолтного
logger.setLevel(logging.DEBUG)


def foo():
    log_level = logger.getEffectiveLevel()
    print(log_level)
    log_msg = "log_message"
    logger.debug(f"debug {log_msg}")
    logger.info(f"info {log_msg}")
    logger.warning(f"warning {log_msg}")
    logger.error(f"error {log_msg}")
    logger.critical(f"critical {log_msg}")


def log_exception():
    try:
        100 / 0
    except ZeroDivisionError as err:
        # записать в лог ошибку с трейсбэком
        logger.error(f"Error {err}", exc_info=err)

        # эквивалент
        # logger.exception(f"Error {err}")


if __name__ == '__main__':
    # foo()
    log_exception()
