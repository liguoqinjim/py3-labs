import logging


def demo():
    logging.basicConfig()
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    demo()
