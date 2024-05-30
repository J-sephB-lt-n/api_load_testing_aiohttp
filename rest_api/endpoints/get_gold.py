"""
Defines endpoint /get_gold
"""

import json
import random
import time

import flask

import config

bp = flask.Blueprint("get_gold", __name__)


@bp.route("/get_gold", methods=["GET"])
def get_gold():
    time.sleep(config.ENDPOINT_PROCESS_TIME_NSECS["/get_task"])
    return flask.jsonify(
        {
            "resource": "gold",
            "amount": random.randint(0, 1),
        }
    )
