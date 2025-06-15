import logging

import sys
from pathlib import Path

# Add the exercises directory to the path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from service import Service

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='[Info] %(message)s')
    
    service = Service()
    result = service.doFirstJob("Hi")
    logging.info(f"Result: {result}")

    result = service.doSecondJob("Hello")
    logging.info(f"Result: {result}")
