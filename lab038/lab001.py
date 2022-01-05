from loguru import logger
import sys


def demo():
    logger.remove()
    # logger.add(sys.stdout, level="INFO", colorize=True, format="{time} {level} {message}" )
    logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>| <level>{message}</level>")

    logger.debug("Debug")
    logger.info("Info")
    logger.error("Error")

    new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")
    logger.log("SNAKY", "Here we go!")

    pass


if __name__ == '__main__':
    demo()
