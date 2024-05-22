import multiprocessing
import logging

logger = logging.getLogger(__name__)


class ProcessPullExecutor:
    def __init__(self, max_workers=None):
        if max_workers is None:
            max_workers = multiprocessing.cpu_count()
            logger.info(f"Using {max_workers} workers")
        self.pool = multiprocessing.Pool(max_workers)
        logger.info("Pool created")

    def submit(self, func, *args, **kwargs):
        logger.info(
            f"Submitting task: {func.__name__} with args: {args} kwargs: {kwargs}")
        return self.pool.apply_async(func, args=args, kwds=kwargs)

    def map(self, func, iterable):
        logger.info(
            f"Mapping function: {func.__name__} over iterable: {iterable}")
        return self.pool.map(func, iterable)

    def shutdown(self):
        logger.info("Shutting down pool")
        self.pool.close()
        self.pool.join()

# # Example usage:
# def square(x):
#     return x * x

# executor = ProcessPullExecutor(max_workers=4)
# result = executor.map(square, range(10))
# print(result)
# executor.shutdown()
