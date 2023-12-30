import logging

logging.basicConfig(level=logging.INFO)
# по дефолту getLogger() возвращает root_logger
root_logger = logging.getLogger()
# так создаётся (если его ещё нет) либо получается (если он уже создан ранее) именованный логгер
my_logger = logging.getLogger("my_logger")
# ему можно задать свой уровень логирования
my_logger.setLevel(logging.DEBUG)


def foo(logger_name_: str | None):
    logger = logging.getLogger(logger_name_)
    logger.debug(f"debug from foo with {logger_name_=}, logger: {logger.name}")
    logger.info(f"info from foo with {logger_name_=}, logger: {logger.name}")


if __name__ == '__main__':
    for logger_name in ("my_logger", None):
        foo(logger_name)
