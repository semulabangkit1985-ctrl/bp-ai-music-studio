"""
SONIQ MASTER AI
Logging configuration.
"""

import logging
import sys


def setup_logging() -> None:
    """
    Configure application logging.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


logger = logging.getLogger("soniq-master-ai")
