#! /usr/bin/env
# -*- coding: utf-8 -*-
# $Id$
import logging
import logging.handlers
from collections import defaultdict as defaultdict
#                     B       K    M
SIZE_1KB = 1024
SIZE_1MB = (1024 * SIZE_1KB)
SIZE_10MB = (10 * SIZE_1MB)
SIZE_1000MB = (100 * SIZE_1MB)
LOG_SIZE_MAX_BYTES = SIZE_10MB

logging.basicConfig(level=logging.DEBUG,
                    # format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='default.log',
                    filemode='a')


loggers_dict = {}

root = logging.getLogger('')
default_logger_h = logging.handlers.RotatingFileHandler(
    'default.log', 'a', LOG_SIZE_MAX_BYTES, 10)
default_logger_h.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "[%(asctime)s-%(levelname)s]:%(name)s:%(funcName)s:%(message)s")
default_logger_h.setFormatter(formatter)

root.addHandler(default_logger_h)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
root.addHandler(console)

default_logger = logging.getLogger('default_app_logger')


def create_logger(name):
    logger = logging.getLogger(name)
    return logger


def get_logger(name=None):
    if name is None:
        return default_logger
    else:
        if name not in loggers_dict.keys():
            loggers_dict[name] = create_logger(name)
    return loggers_dict[name]


def main():
    # test the loggers functionality
    loggerwa = get_logger()
    loggerwa.info("loggerwa")

    logerwa2 = get_logger('loggerwa_2')
    logerwa2.info('logerwa2')

    loggerwa3 = get_logger('loggerwa_2')
    loggerwa3.debug('loggerwa3')


if __name__ == '__main__':
    main()
