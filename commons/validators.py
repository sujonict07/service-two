from uuid import UUID

from .utils import get_logger

logger = get_logger()


def validate_uuid4(uuid_string):
    try:
        logger.info(UUID(uuid_string, version=4))
    except Exception as e:
        logger.error("Invalid uuid {}".format(e))
        return False
    return True
