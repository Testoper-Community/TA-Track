import json
import logging

from library.custom_logger import customLogger as cl

log = cl(logging.DEBUG)


def print_log(response):
    log.info(json.dumps(response.json()))


def headers():
    contentType = {
        "Content-Type: application/json; charset=UTF-8"
    }
