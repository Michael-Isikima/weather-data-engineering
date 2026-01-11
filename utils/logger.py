# utils/logger.py
import logging
import sys

def get_logger(name: str):
    logger = logging.getLogger(name)  # create a dynamic logger
    logger.setLevel(logging.INFO)     # setting logger levels

    if not logger.handlers:             # checking if handles exists
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )                                                               #formatting logger response

        handler = logging.StreamHandler(sys.stdout)                     # setting logger output (terminal)
        handler.setFormatter(formatter)                                 # attaching logger format to handler

        logger.addHandler(handler)                                      # attaching handler to logger

    return logger                                                       # retun logger so it can be called.
