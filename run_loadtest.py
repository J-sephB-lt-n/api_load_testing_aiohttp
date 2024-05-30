"""
docstring TODO

Example Usage:
$ python run_loadtest.py --service_url $CLOUD_RUN_SERVICE_URL
"""

import argparse
import asyncio
import logging
import os
from typing import Final

import aiohttp

import loadtest_config
from worker import Worker

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "-u",
    "--service_url",
    help="URL of the deployed cloud run service hosting the project endpoints",
    type=str,
    required=True,
)
args = arg_parser.parse_args()

# set up python logger #
if os.path.exists("logs/loadtest.log"):
    os.remove("logs/loadtest.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/loadtest.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


async def main():
    # async with aiohttp.ClientSession(
    #    connector=aiohttp.TCPConnector(limit=1000)
    # ) as session:
    workers: list[Worker] = [
        Worker(
            id=idx,
            lifetime=loadtest_config.N_TASKS_PER_WORKER,
            # session=session,
            service_url=args.service_url,
        )
        for idx in range(loadtest_config.N_WORKERS)
    ]
    tasks = [worker.work() for worker in workers]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
