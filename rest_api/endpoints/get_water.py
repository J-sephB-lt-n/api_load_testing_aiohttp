"""
Defines endpoint /get_water
"""

import json
import random
import time

import flask

import config

bp = flask.Blueprint("get_water", __name__)


@bp.route("/get_water", methods=["GET"])
def get_water():
    time.sleep(config.ENDPOINT_PROCESS_TIME_NSECS["/get_task"])
    return flask.jsonify(
        {
            "resource": "water",
            "amount": random.randint(0, 10),
        }
    )
