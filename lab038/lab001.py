from loguru import logger
import sys


def demo():
    logger.remove()
    # logger.add(sys.stdout, level="INFO", colorize=True, format="{time} {level} {message}" )
    logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green>| <level>{message}</level>")

    logger.remove()
    # logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>|</red> <level>{level: <2}</level> <red>|</red> <cyan>{function}</cyan> <red>-</red> <level>{message}</level>")
    logger.add(sys.stdout, colorize=True,
               format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red>|</red> <level>{level: <6}</level> <red>|</red> <level>{message}</level>")

    # logger.add(sys.stdout, colorize=True, format="<green>{time:YYYY-MM-DD HH:mm:ss.}</green> <red>|</red> "
    #                                              "<level>{level: <8}</level> <red>|</red> "
    #                                              "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>", )

    logger.debug("Debug")
    logger.info("Info")
    logger.error("Error")

    new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")
    logger.log("SNAKY", "Here we go!")

    pass


if __name__ == '__main__':
    demo()
