import subprocess
from logger_format import setup_logging

logger = setup_logging(__file__)


try:
    logger.info("Start", exc_info=True)
    o=2/0
    logger.info("END ", exc_info=False)
except Exception as e:
    logger.exception("Failed end", exc_info=True)