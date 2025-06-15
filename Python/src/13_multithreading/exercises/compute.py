import time
from concurrent.futures import ThreadPoolExecutor
from random import random

NUMBER_OF_ELEMENTS = 10_000
NUMBER_OF_THREADS = 10
PARTITION_SIZE = 1_000


def find_min_parallel(numbers: list[float]) -> float:
    """
    Finds the minimum value in a list of numbers in parallel using multiple threads.
    The list is partitioned into smaller segments, and each segment is processed
    by a separate thread. The results are then combined to get the final minimum.

    :param numbers: The list of numbers to find the minimum value.
    """
    min_value = float("inf")
    futures = list()
    with ThreadPoolExecutor(NUMBER_OF_THREADS) as executor:
        for i in range(0, len(numbers), PARTITION_SIZE):
            index_start = i
            index_end_incl = min(i + PARTITION_SIZE, len(numbers))
            futures.append(
                executor.submit(
                    find_min_sequential, numbers, index_start, index_end_incl
                )
            )
    for future in futures:
        min_value = min(min_value, future.result())
    return min_value


def find_min_sequential(
    numbers: list[float], index_start: int, index_end_excl: int
) -> float:
    """
    Finds the minimum value of a segment of a list of numbers sequentially.

    :param numbers: The list of numbers to find the minimum value.
    :param index_start: The starting index of the segment.
    :param index_end_excl: The ending index (exclusive) of the segment.
    """
    local_min = float("inf")
    for i in range(index_start, index_end_excl):
        local_min = min(local_min, numbers[i])
    return local_min


if __name__ == "__main__":

    def measure_execution_time(name, func, *args):
        start = time.time_ns()
        result = func(*args)
        duration_ms = (time.time_ns() - start) / 1_000

        print(f"[{name}] Duration: {duration_ms} ms | Result {result}")

    numbers = [random() * 100 for _ in range(NUMBER_OF_ELEMENTS)]

    measure_execution_time(
        " Sequential ", find_min_sequential, numbers, 0, len(numbers)
    )

    measure_execution_time(" Parallel   ", find_min_parallel, numbers)
