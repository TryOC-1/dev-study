import os
import sys
import logging
from datetime import datetime

LOGDIR = "log"


def set_logger():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    logformat = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    # Add stream handler
    ch = logging.StreamHandler()
    ch.setFormatter(logformat)
    log.addHandler(ch)

    # Add file handler
    os.makedirs(LOGDIR, exist_ok=True)
    today_str = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(LOGDIR, today_str + ".log")
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logformat)
    log.addHandler(fh)
