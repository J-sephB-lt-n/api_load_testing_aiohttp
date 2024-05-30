"""
Defines endpoint /get_water
"""

import json
import random
import time

import flask

import loadtest_config

bp = flask.Blueprint("get_water", __name__)


@bp.route("/get_water", methods=["GET"])
def get_water():
    time.sleep(loadtest_config.ENDPOINT_PROCESS_TIME_NSECS["/get_task"])
    return flask.Response(
        json.dumps(
            {
                "resource": "water",
                "amount": random.randint(0, 10),
            }
        ),
        status=200,
    )
