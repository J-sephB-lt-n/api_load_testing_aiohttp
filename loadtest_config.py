"""
Parameters controlling aspects of the load test
"""
from typing import Final

N_WORKERS: Final[int] = 1_000
N_TASKS_PER_WORKER: Final[int] = 10 

ENDPOINT_PROCESS_TIME_NSECS = {
    # passed to time.sleep() to increase the
    # endpoint response time
    "/get_task": 1,
    "/get_gold": 1,
    "/get_oil": 1,
    "/get_water": 1,
    "/deposit_resource": 1,
}
