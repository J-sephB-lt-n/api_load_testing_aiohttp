"""
Parameters controlling endpoint behaviour
"""

ENDPOINT_PROCESS_TIME_NSECS = {
    # passed to time.sleep() to increase the
    # endpoint response time
    "/get_task": 1,
    "/get_gold": 1,
    "/get_oil": 1,
    "/get_water": 1,
    "/deposit_resource": 1,
}
