"""
The Worker() class
"""

import logging

import aiohttp

logger = logging.getLogger(__name__)


class Worker:
    """A single automated endpoint user (for load-testing)"""

    def __init__(
        self, id: str, lifetime: int, session: aiohttp.ClientSession, service_url: str
    ) -> None:
        """Define attributes at instantiation"""
        self.id = id
        self.session = session
        self.request_count = 0
        self.success_task_count = 0
        self.failed_task_count = 0
        self.lifetime = lifetime
        self.service_url = service_url

    async def work(self):
        """
        Repeatedly use the endpoints as follows:
            1. Call /get_task to be assigned a resource to fetch
            2. Fetch assigned resource using one of:
                a. /get_gold
                b. /get_oil
                c. /get_water
            3. If received a non-zero amount of resource, deposit
                it using /deposit_resource
            4. If we've completed `self.lifetime` tasks then stop,
                otherwise repeat from step (1)
        """
        while (self.success_task_count + self.failed_task_count) < self.lifetime:
            async with self.session.get(f"{self.service_url}/get_task") as resp:
                self.request_count += 1
                logger.info(
                    "worker |%s| request [%s] to /get_task", self.id, self.request_count
                )
                task = await resp.text()
                logger.info(
                    "worker |%s| request [%s] had status {%s}",
                    self.id,
                    self.request_count,
                    resp.status,
                )
                if resp.status != 200:
                    self.failed_task_count += 1
                    continue
                logger.info(
                    "worker |%s| request [%s] received task [%s]",
                    self.id,
                    self.request_count,
                    task,
                )
            async with self.session.get(f"{self.service_url}/{task}") as resp:
                self.request_count += 1
                logger.info(
                    "worker |%s| request [%s] to /%s", self.id, self.request_count, task
                )
                resource_received = await resp.json()
                logger.info(
                    "worker |%s| request [%s] had status {%s}",
                    self.id,
                    self.request_count,
                    resp.status,
                )
                if resp.status != 200:
                    self.failed_task_count += 1
                    continue
                logger.info(
                    "worker |%s| request [%s] received %s units of %s",
                    self.id,
                    self.request_count,
                    resource_received["amount"],
                    resource_received["resource"],
                )
            if resource_received["amount"] > 0:
                async with self.session.post(
                    f"{self.service_url}/deposit_resource",
                    json={
                        "resource": resource_received["resource"],
                        "amount": int(resource_received["amount"]),
                    },
                ) as resp:
                    self.request_count += 1
                    logger.info(
                        "worker |%s| request [%s] to /deposit_resource",
                        self.id,
                        self.request_count,
                    )
                    deposit_status = await resp.json()
                    logger.info(
                        "worker |%s| request [%s] had status {%s}",
                        self.id,
                        self.request_count,
                        resp.status,
                    )
                    if resp.status != 200:
                        self.failed_task_count += 1
                        continue
                    logger.info(
                        "worker |%s| request [%s] received deposit status %s",
                        self.id,
                        self.request_count,
                        deposit_status,
                    )
            self.success_task_count += 1
            logging.info("worker |%s| has successfully completed %s tasks", self.id, self.success_task_count)
