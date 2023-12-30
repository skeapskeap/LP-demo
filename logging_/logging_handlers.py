import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG)
root_logger = logging.getLogger()
file_logger = logging.getLogger("my_log")
# чтобы сообщения file_logger не обрабатывались хэндлерами родительского логгера (root_logger)
file_logger.propagate = False

# создать хэндлер, который записывает логи в файл
file_handler = RotatingFileHandler(filename='log_file', mode='a', maxBytes=512, backupCount=3)
# задать формат логов для нового хэндлера
custom_formatter = logging.Formatter("%(asctime)s | %(levelname)10s | %(name)10s : %(message)s")
file_handler.setFormatter(custom_formatter)
# добавить созданный хэндлер в file_logger
file_logger.addHandler(file_handler)


def foo():
    for i in range(100):
        # root_logger пишет в stdout с дефолтным форматированием
        root_logger.debug(f"message from root logger; message_num: {i}")
        # file_logger пишет в файл с кастомным форматированием
        file_logger.debug(f"message from my logger; message_num: {i}")


if __name__ == '__main__':
    foo()
