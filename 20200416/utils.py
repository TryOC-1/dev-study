import os
import sys
import logging
from datetime import datetime

LOGDIR = "log"


def set_logger():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    # TODO: Set log formatter

    # TODO: Add stream handler

    # TODO: Add file handler
    os.makedirs(LOGDIR, exist_ok=True)
    today_str = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(LOGDIR, today_str + ".log")
