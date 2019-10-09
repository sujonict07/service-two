import random
import string
import logging
import os
from rest_framework import status
# from myapplication.settings import CUSTOM_LOG

msg = {"invalid": "invalid Request"}

GET_BY_ID = 'id'
GET_BY_UUID = 'uuid'
GET_INSTANCE = GET_BY_UUID

support_method = {'post': 'create'}
retrieve_method = {'get': 'retrieve',
                   'put': 'update',
                   'patch': 'partial_update',
                   'delete': 'destroy'
                   }


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def deleted_response(uuid, status=status.HTTP_204_NO_CONTENT):
    return {
        "uuid": uuid,
        "status": status
    }


def string_to_boolean(string):
    try:
        return not eval(string.title())
    except NameError:
        return True


def delete_file(path):
    try:
        os.remove(path)
    except OSError:
        pass

def get_logger(name=None):
    if name is None:
        name = ""
    logger = logging.getLogger(name=name)
    return logger
