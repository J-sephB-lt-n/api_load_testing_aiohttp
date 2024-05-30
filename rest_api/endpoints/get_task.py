"""
Defines endpoint /get_task
"""

import random
import time

import flask

import config

bp = flask.Blueprint("get_task", __name__)


@bp.route("/get_task", methods=["GET"])
def get_task():
    """TODO"""
    time.sleep(config.ENDPOINT_PROCESS_TIME_NSECS["/get_task"])
    return flask.Response(
        random.choice(("get_gold", "get_oil", "get_water")), status=200
    )
