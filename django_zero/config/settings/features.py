import logging
import os
from functools import lru_cache

from django_zero.utils import get_bool_from_env

logger = logging.getLogger(__name__)


@lru_cache()
def is_celery_enabled():
    celery_enabled = get_bool_from_env("ENABLE_CELERY", default=False)
    logger.debug("Celery: %s", "enabled" if celery_enabled else "disabled")
    return celery_enabled


_celery_loglevels = "DEBUG|INFO|WARNING|ERROR|CRITICAL|FATAL".split("|")


def get_celery_beat_loglevel():
    loglevel = os.environ.get("CELERY_BEAT_LOGLEVEL")
    if loglevel.upper() in _celery_loglevels:
        return loglevel.lower()


def get_celery_worker_loglevel():
    loglevel = os.environ.get("CELERY_WORKER_LOGLEVEL")
    if loglevel.upper() in _celery_loglevels:
        return loglevel.lower()


@lru_cache()
def is_channels_enabled():
    channels_enabled = get_bool_from_env("ENABLE_CHANNELS", default=False)
    logger.debug("Channels: %s", "enabled" if channels_enabled else "disabled")
    return channels_enabled


@lru_cache()
def is_whitenoise_enabled():
    whitenoise_enabled = get_bool_from_env("ENABLE_WHITENOISE", default=True)
    logger.debug("Whitenoise: %s", "enabled" if whitenoise_enabled else "disabled")
    return whitenoise_enabled


@lru_cache()
def is_webpack_enabled():
    webpack_enabled = get_bool_from_env("ENABLE_WEBPACK", default=True)
    logger.debug("Webpack: %s", "enabled" if webpack_enabled else "disabled")
    return webpack_enabled
