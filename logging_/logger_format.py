import logging

# https://docs.python.org/3/library/logging.html#logrecord-attributes
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s | %(levelname)10s | %(name)10s : %(message)s")

root_logger = logging.getLogger()


def foo():
    root_logger.info("message from root")


if __name__ == '__main__':
    foo()
