"""
TODO

Example Usage:
$ poetry run python run_loadtest.py
"""

import asyncio
import logging
import os
from typing import Final

import aiohttp

# set up python logger #
if os.path.exists("logs/loadtest.log"):
    os.remove("logs/loadtest.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/loadtest.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

import loadtest_config
from worker import Worker


async def main():
    async with aiohttp.ClientSession() as session:
        workers: list[Worker] = [
            Worker(id=idx, lifetime=loadtest_config.N_TASKS_PER_WORKER, session=session)
            for idx in range(loadtest_config.N_WORKERS)
        ]
        tasks = [worker.work() for worker in workers]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
