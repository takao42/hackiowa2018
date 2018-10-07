import logging
import json


def to_int(val):
    try:
        return int(val)
    except ValueError:
        return None


def make_logger(name, default_level=logging.DEBUG, file_name=None):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')
    logger.setLevel(default_level)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    if file_name:
        file_handler = logging.FileHandler(file_name)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger


def print_dict(data):
    print(json.dumps(data, indent=4))
