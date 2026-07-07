from __future__ import annotations

import logging
import sys

from pythonjsonlogger.json import JsonFormatter

from app.core.settings import settings


def configure_logging() -> None:
    """
    Configure application logging.
    """

    handler = logging.StreamHandler(sys.stdout)

    formatter = JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    handler.setFormatter(formatter)

    logging.basicConfig(
        level=settings.log_level,
        handlers=[handler],
        force=True,
    )