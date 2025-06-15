import logging

import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from logging_aspect import log_injection

class Service:
    def __init__(self):
        pass

    @log_injection
    def doFirstJob(self, param: str) -> str:
        logging.info(f"Executing first job with {param}")
        return param

    @log_injection
    def doSecondJob(self, param: str) -> str:
        logging.info(f"Executiing second job with {param}")
        return param
