import logging
import time

import aspectlib


@aspectlib.Aspect
def log_injection(*args, **kwargs):
    start = time.perf_counter_ns()

    _log_gray(f"Before call of '{type(args[0]).__name__}'-Class with args: {args[1:]} and kwargs: {kwargs}")

    result = yield aspectlib.Proceed

    _log_gray(f"After call | Duration {(time.perf_counter_ns() - start) / 1000} ms")

    return result

def _log_gray(message: str):
    """
    Log a message in gray color.
    """
    logging.info(f"\033[90m{message}\033[0m")
